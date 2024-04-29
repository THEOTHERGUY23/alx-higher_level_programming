#!/bin/bash

# Check if the URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command-line argument
URL=$1

# Send a GET request to the URL and display the body of the response
curl -s "$URL"
