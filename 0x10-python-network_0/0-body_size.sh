#!/bin/bash
# Script that takes in URL, sends request and displays size of body of response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
