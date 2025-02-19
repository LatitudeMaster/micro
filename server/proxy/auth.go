package proxy

import (
	"context"
	"strings"

	inAuth "github.com/micro-community/micro/v3/platform/auth"
	inAuthNamespace "github.com/micro-community/micro/v3/platform/auth/namespace"

	"github.com/micro-community/micro/v3/service/auth"
	"github.com/micro-community/micro/v3/service/context/metadata"
	"github.com/micro-community/micro/v3/service/errors"
	"github.com/micro-community/micro/v3/service/server"
)

// authHandler wraps a server handler to perform auth
func authHandler() server.HandlerWrapper {
	return func(h server.HandlerFunc) server.HandlerFunc {
		return func(ctx context.Context, req server.Request, rsp interface{}) error {
			// Extract the token if the header is present. We will inspect the token regardless of if it's
			// present or not since noop auth will return a blank account upon Inspecting a blank token.
			var token string
			if header, ok := metadata.Get(ctx, "Authorization"); ok {
				// Ensure the correct scheme is being used
				if !strings.HasPrefix(header, inAuth.BearerScheme) {
					return errors.Unauthorized(req.Service(), "invalid authorization header. expected Bearer schema")
				}

				// Strip the bearer scheme prefix
				token = strings.TrimPrefix(header, inAuth.BearerScheme)
			}

			// Inspect the token and decode an account
			account, _ := auth.Inspect(token)

			// Extract the namespace header
			ns, ok := metadata.Get(ctx, "Micro-Namespace")
			if !ok && account != nil {
				ns = account.Issuer
				ctx = metadata.Set(ctx, "Micro-Namespace", ns)
			} else if !ok {
				ns = inAuthNamespace.DefaultNamespace
				ctx = metadata.Set(ctx, "Micro-Namespace", ns)
			}

			// construct the resource
			res := &auth.Resource{
				Type:     "service",
				Name:     req.Service(),
				Endpoint: req.Endpoint(),
			}

			// Verify the caller has access to the resource.
			err := auth.Verify(account, res, auth.VerifyNamespace(ns))
			if err == auth.ErrForbidden && account != nil {
				return errors.Forbidden(req.Service(), "Forbidden call made to %v:%v by %v", req.Service(), req.Endpoint(), account.ID)
			} else if err == auth.ErrForbidden {
				return errors.Unauthorized(req.Service(), "Unauthorized call made to %v:%v", req.Service(), req.Endpoint())
			} else if err != nil {
				return errors.InternalServerError("proxy", "Error authorizing request: %v", err)
			}

			// The user is authorized, allow the call
			return h(ctx, req, rsp)
		}
	}
}
