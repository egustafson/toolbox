package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"net/http"

	log "github.com/sirupsen/logrus"
)

var (
	port = flag.Int("port", 8080, "listen on port (default: 8080)")
	resp = flag.Int("resp", 200, "HTTP response code (default: 200")
)

func snoopHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("\n--- new request --->")
	fmt.Printf("method:  %s\n", r.Method)
	fmt.Printf("uri:     %s\n", r.RequestURI)
	fmt.Printf("Host:    %s\n", r.Host)
	for k, values := range r.Header {
		if len(values) < 2 {
			fmt.Printf(" %s:  %s\n", k, values[0])
		} else {
			fmt.Printf(" %s: ", k)
			preamble := "{"
			for _, v := range values {
				fmt.Printf("%s%s", preamble, v)
				preamble = ", "
			}
			fmt.Println("}")
		}
	}

	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("\n%s\n", body)

	fmt.Println("<----------")
	fmt.Printf("response:  %d\n\n", *resp)
	w.WriteHeader(*resp)
}

func main() {
	flag.Parse()
	laddr := fmt.Sprintf(":%d", *port) // 0.0.0.0:[port]
	s := &http.Server{
		Addr:    laddr,
		Handler: http.HandlerFunc(snoopHandler),
	}
	log.Infof("Start - listening to: %d", laddr)
	log.Fatal(s.ListenAndServe())
}
