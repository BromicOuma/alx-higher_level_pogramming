#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" -X OPTIONS | grep "allow:"   | cut -d ":" -f2  | sed 's/ //'
