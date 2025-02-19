// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Original source: github.com/micro/go-micro/v3/network/resolver/http/http.go

// Package http resolves names to network addresses using a http request
package http

import (
	"encoding/json"
	"errors"
	"io/ioutil"
	"net/http"
	"net/url"

	"github.com/micro-community/micro/v3/platform/network/resolver"
)

// Resolver is a HTTP network resolver
type Resolver struct {
	// If not set, defaults to http
	Proto string

	// Path sets the path to lookup. Defaults to /network
	Path string

	// Host url to use for the query
	Host string
}

type Response struct {
	Nodes []*resolver.Record `json:"nodes,omitempty"`
}

// Resolve assumes ID is a domain which can be converted to a http://name/network request
func (r *Resolver) Resolve(name string) ([]*resolver.Record, error) {
	proto := "http"
	host := "localhost:8080"
	path := "/network/nodes"

	if len(r.Proto) > 0 {
		proto = r.Proto
	}

	if len(r.Path) > 0 {
		path = r.Path
	}

	if len(r.Host) > 0 {
		host = r.Host
	}

	uri := &url.URL{
		Scheme: proto,
		Path:   path,
		Host:   host,
	}
	q := uri.Query()
	q.Set("name", name)
	uri.RawQuery = q.Encode()

	rsp, err := http.Get(uri.String())
	if err != nil {
		return nil, err
	}
	defer rsp.Body.Close()
	if rsp.StatusCode != 200 {
		return nil, errors.New("non 200 response")
	}
	b, err := ioutil.ReadAll(rsp.Body)
	if err != nil {
		return nil, err
	}

	// encoding format is assumed to be json
	var response *Response

	if err := json.Unmarshal(b, &response); err != nil {
		return nil, err
	}

	return response.Nodes, nil
}
