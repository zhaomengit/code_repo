package main

import (
    "errors"
    "net"
    "time"
)

// 自定义Listener,增加停止channel和设置超时时间
// stoppableListener sets TCP keep-alive timeouts on accepted
// connections and waits on stopc message
type stoppableListener struct {
    *net.TCPListener
    stopc <-chan struct{}
}

func newStoppableListener(addr string, stopc <-chan struct{}) (*stoppableListener, error) {
    ln, err := net.Listen("tcp", addr)
    if err != nil {
        return nil, err
    }
    return &stoppableListener{ln.(*net.TCPListener), stopc}, nil
}

func (ln stoppableListener) Accept() (c net.Conn, err error) {
    connc := make(chan *net.TCPConn, 1)
    errc := make(chan error, 1)
    go func() {
        tc, err := ln.AcceptTCP()
        if err != nil {
            errc <- err
            return
        }
        connc <- tc
    }()
    select {
    case <-ln.stopc:
        return nil, errors.New("server stopped")
    case err := <-errc:
        return nil, err
    case tc := <-connc:
        tc.SetKeepAlive(true)
        tc.SetKeepAlivePeriod(3 * time.Minute)
        return tc, nil
    }
}

/*
ln, err := newStoppableListener(Host, httpstopc)
	if err != nil {
		log.Fatalf("Failed to listen (%v)", err)
	}

	err = (&http.Server{Handler: rc.transport.Handler()}).Serve(ln)
	select {
	case <- httpstopc:
	default:
		log.Fatalf(": Failed to serve (%v)", err)
	}
  */
