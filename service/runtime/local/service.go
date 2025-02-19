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
// Original source: github.com/micro/go-micro/v3/runtime/local/service.go

package local

import (
	"fmt"
	"io"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/micro-community/micro/v3/platform/build"
	"github.com/micro-community/micro/v3/service/logger"
	"github.com/micro-community/micro/v3/service/runtime"
	"github.com/micro-community/micro/v3/service/runtime/local/process"
	proc "github.com/micro-community/micro/v3/service/runtime/local/process/os"
)

type service struct {
	sync.RWMutex

	running bool
	closed  chan bool
	err     error
	updated time.Time

	retries    int
	maxRetries int

	// output for logs
	output io.Writer

	// service to manage
	*runtime.Service
	// process creator
	Process *proc.Process
	// Exec
	Exec *process.Binary
	// process pid
	PID *process.PID
}

func newService(s *runtime.Service, c runtime.CreateOptions) *service {
	var exec string
	var args []string

	// set command
	exec = strings.Join(c.Command, " ")
	args = c.Args

	dir := s.Source

	return &service{
		Service: s,
		Process: new(proc.Process),
		Exec: &process.Binary{
			Package: &build.Package{
				Name: s.Name,
				Path: exec,
			},
			Env:  c.Env,
			Args: args,
			Dir:  dir,
		},
		closed:     make(chan bool),
		output:     c.Output,
		updated:    time.Now(),
		maxRetries: c.Retries,
	}
}

func (s *service) streamOutput() {
	go io.Copy(s.output, s.PID.Output)
	go io.Copy(s.output, s.PID.Error)
}

func (s *service) shouldStart() bool {
	if s.running {
		return false
	}
	return s.retries <= s.maxRetries
}

func (s *service) key() string {
	return fmt.Sprintf("%v:%v", s.Name, s.Version)
}

func (s *service) ShouldStart() bool {
	s.RLock()
	defer s.RUnlock()
	return s.shouldStart()
}

func (s *service) Running() bool {
	s.RLock()
	defer s.RUnlock()
	return s.running
}

// Start starts the service
func (s *service) Start() error {
	s.Lock()
	defer s.Unlock()

	if !s.shouldStart() {
		return nil
	}

	// reset
	s.err = nil
	s.closed = make(chan bool)
	s.retries = 0

	if s.Metadata == nil {
		s.Metadata = make(map[string]string)
	}
	s.Status(runtime.Starting, nil)

	// TODO: pull source & build binary
	if logger.V(logger.DebugLevel, logger.DefaultLogger) {
		logger.Debugf("Runtime service %s forking new process", s.Service.Name)
	}

	p, err := s.Process.Fork(s.Exec)
	if err != nil {
		s.Status(runtime.Error, err)
		return err
	}
	// set the pid
	s.PID = p
	// set to running
	s.running = true
	// set status
	s.Status(runtime.Running, nil)
	// set started
	s.Metadata["started"] = time.Now().Format(time.RFC3339)

	if s.output != nil {
		s.streamOutput()
	}

	// wait and watch
	go func() {
		s.Wait()

		logger.Infof("Service %s has stopped", s.Service.Name)

		// don't do anything if it was stopped
		if s.Service.Status == runtime.Stopped {
			return
		}

		// should we restart?
		if !s.shouldStart() {
			return
		}

		logger.Infof("Restarting service %s", s.Service.Name)

		// restart the process
		s.Start()
	}()

	return nil
}

// Status updates the status of the service. Assumes it's called under a lock as it mutates state
func (s *service) Status(status runtime.ServiceStatus, err error) {
	s.Service.Status = status
	s.Metadata["lastStatusUpdate"] = time.Now().Format(time.RFC3339)
	if err == nil {
		delete(s.Metadata, "error")
		return
	}
	s.Metadata["error"] = err.Error()

}

// Stop stops the service
func (s *service) Stop() error {
	s.Lock()
	defer s.Unlock()

	select {
	case <-s.closed:
		return nil
	default:
		close(s.closed)
		s.running = false
		s.retries = 0
		if s.PID == nil {
			return nil
		}

		// set status
		s.Status(runtime.Stopping, nil)

		// kill the process
		err := s.Process.Kill(s.PID)
		if err == nil {
			// wait for it to exit
			s.Process.Wait(s.PID)
		}

		// set status
		s.Status(runtime.Stopped, err)

		// return the kill error
		return err
	}
}

// Error returns the last error service has returned
func (s *service) Error() error {
	s.RLock()
	defer s.RUnlock()
	return s.err
}

// Wait waits for the service to finish running
func (s *service) Wait() {
	// wait for process to exit
	s.RLock()
	thisPID := s.PID
	s.RUnlock()
	err := s.Process.Wait(thisPID)

	s.Lock()
	defer s.Unlock()

	if s.PID.ID != thisPID.ID {
		// trying to update when it's already been switched out, ignore
		logger.Debugf("Trying to update a process status but PID doesn't match. Old %s, New %s. Skipping update.", thisPID.ID, s.PID.ID)
		return
	}

	// save the error
	if err != nil {
		if logger.V(logger.ErrorLevel, logger.DefaultLogger) {
			logger.Errorf("Service %s terminated with error %s", s.Name, err)
		}
		s.retries++
		s.Status(runtime.Error, err)
		s.Metadata["retries"] = strconv.Itoa(s.retries)

		s.err = err
	} else {
		// check if it was stopped
		if s.Service.Status != runtime.Stopped {
			s.Status(runtime.Error, fmt.Errorf("Service %s terminated", s.Name))
		}
	}

	// no longer running
	s.running = false
}
