package template

var (
	Module = `module {{.Dir}}

go 1.15

require (
	github.com/micro-community/micro/v3 v3.2.0
)

// This can be removed once etcd becomes go gettable, version 3.4 and 3.5 is not,
// see https://github.com/etcd-io/etcd/issues/11154 and https://github.com/etcd-io/etcd/issues/11931.
replace google.golang.org/grpc => google.golang.org/grpc v1.29.0
`
)
