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
// Original source: github.com/micro/go-micro/v3/debug/profile/pprof/pprof.go

// Package pprof provides a pprof profiler which writes output to /tmp/[name].{cpu,mem}.pprof
package pprof

import (
	"os"
	"path/filepath"
	"runtime"
	"runtime/pprof"
	"sync"
	"time"

	"github.com/micro-community/micro/v3/platform/debug/profile"
)

type profiler struct {
	opts profile.Options

	sync.Mutex
	running bool
	exit    chan bool

	// where the cpu profile is written
	cpuFile *os.File
	// where the mem profile is written
	memFile *os.File
}

func (p *profiler) writeHeap(f *os.File) {
	defer f.Close()

	t := time.NewTicker(time.Second * 30)
	defer t.Stop()

	for {
		select {
		case <-t.C:
			runtime.GC()
			pprof.WriteHeapProfile(f)
		case <-p.exit:
			return
		}
	}
}

func (p *profiler) Start() error {
	p.Lock()
	defer p.Unlock()

	if p.running {
		return nil
	}

	// create exit channel
	p.exit = make(chan bool)

	cpuFile := filepath.Join("/tmp", "cpu.pprof")
	memFile := filepath.Join("/tmp", "mem.pprof")

	if len(p.opts.Name) > 0 {
		cpuFile = filepath.Join("/tmp", p.opts.Name+".cpu.pprof")
		memFile = filepath.Join("/tmp", p.opts.Name+".mem.pprof")
	}

	f1, err := os.Create(cpuFile)
	if err != nil {
		return err
	}

	f2, err := os.Create(memFile)
	if err != nil {
		return err
	}

	// start cpu profiling
	if err := pprof.StartCPUProfile(f1); err != nil {
		return err
	}

	// write the heap periodically
	go p.writeHeap(f2)

	// set cpu file
	p.cpuFile = f1
	// set mem file
	p.memFile = f2

	p.running = true

	return nil
}

func (p *profiler) Stop() error {
	p.Lock()
	defer p.Unlock()

	select {
	case <-p.exit:
		return nil
	default:
		close(p.exit)
		pprof.StopCPUProfile()
		p.cpuFile.Close()
		p.running = false
		p.cpuFile = nil
		p.memFile = nil
		return nil
	}
}

func (p *profiler) String() string {
	return "pprof"
}

func NewProfile(opts ...profile.Option) profile.Profile {
	var options profile.Options
	for _, o := range opts {
		o(&options)
	}
	p := new(profiler)
	p.opts = options
	return p
}
