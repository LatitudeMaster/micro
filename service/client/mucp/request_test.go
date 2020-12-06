// Copyright 2020 Asim Aslam
//
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
// Original source: github.com/micro/go-micro/v3/client/mucp/mucp_request_test.go

package mucp

import (
	"testing"

	"github.com/micro-community/micro/v3/service/client"
)

func TestRequestOptions(t *testing.T) {
	r := newRequest("service", "endpoint", nil, "application/json")
	if r.Service() != "service" {
		t.Fatalf("expected 'service' got %s", r.Service())
	}
	if r.Endpoint() != "endpoint" {
		t.Fatalf("expected 'endpoint' got %s", r.Endpoint())
	}
	if r.ContentType() != "application/json" {
		t.Fatalf("expected 'endpoint' got %s", r.ContentType())
	}

	r2 := newRequest("service", "endpoint", nil, "application/json", client.WithContentType("application/protobuf"))
	if r2.ContentType() != "application/protobuf" {
		t.Fatalf("expected 'endpoint' got %s", r2.ContentType())
	}
}
