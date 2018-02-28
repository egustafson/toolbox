#!/bin/sh

curl -i \
     -H "Accept: application/json" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{"key": "value"}' \
     http://localhost:8080/foo/bar
