package handler

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/micro-community/micro/v3/profile"
	"github.com/micro-community/micro/v3/service"
	"github.com/micro-community/micro/v3/service/context/metadata"
)

type TestHandler struct {
	t      *testing.T
	expect metadata.Metadata
}

type TestRequest struct{}
type TestResponse struct{}

func (t *TestHandler) Exec(ctx context.Context, req *TestRequest, rsp *TestResponse) error {
	md, ok := metadata.FromContext(ctx)
	if !ok {
		return fmt.Errorf("Expected metadata got %t", ok)
	}

	for k, v := range t.expect {
		if val := md[k]; val != v {
			return fmt.Errorf("Expected %s for key %s got %s", v, k, val)
		}
	}

	t.t.Logf("Received request %+v", req)
	t.t.Logf("Received metadata %+v", md)

	return nil
}

func TestRPCHandler(t *testing.T) {
	profile.Test.Setup(nil)

	srv := service.New(
		service.Name("test"),
	)

	srv.Server().Handle(
		srv.Server().NewHandler(&TestHandler{t, metadata.Metadata{"Foo": "Bar"}}),
	)

	if err := srv.Server().Start(); err != nil {
		t.Fatal(err)
	}

	defer srv.Server().Stop()

	w := httptest.NewRecorder()

	request := map[string]string{
		"service":  "test",
		"endpoint": "TestHandler.Exec",
		"request":  "{}",
	}

	rb, err := json.Marshal(request)
	if err != nil {
		t.Fatal(err)
	}

	b := bytes.NewBuffer(rb)

	req, err := http.NewRequest("POST", "/rpc", b)
	if err != nil {
		t.Fatal(err)
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Foo", "Bar")

	NewRPCHandler(nil).ServeHTTP(w, req)

	if w.Code != 200 {
		t.Fatalf("Expected 200 response got %d %s", w.Code, w.Body.String())
	}
}
