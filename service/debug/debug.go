package debug

import (
	"github.com/micro-community/micro/v3/util/debug/log"
	memLog "github.com/micro-community/micro/v3/util/debug/log/memory"
	"github.com/micro-community/micro/v3/util/debug/profile"
	"github.com/micro-community/micro/v3/util/debug/stats"
	memStats "github.com/micro-community/micro/v3/util/debug/stats/memory"
	"github.com/micro-community/micro/v3/util/debug/trace"
	memTrace "github.com/micro-community/micro/v3/util/debug/trace/memory"
)

// export default
var (
	DefaultLog      log.Log         = memLog.NewLog()
	DefaultTracer   trace.Tracer    = memTrace.NewTracer()
	DefaultStats    stats.Stats     = memStats.NewStats()
	DefaultProfiler profile.Profile = nil
)
