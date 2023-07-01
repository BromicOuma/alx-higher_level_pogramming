#!/bin/bash
#  Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -D ./header -o ./output; if grep --silent "200 OK" ./header; then cat ./output; fi
