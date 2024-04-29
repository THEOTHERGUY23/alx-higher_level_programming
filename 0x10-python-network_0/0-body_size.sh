#!/bin/bash

# Check if the URL is provided as an argument

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Get the URL from the command-line argument
URL=$1

SIZE=$(curl -sI "$URL" | grep -i 'content-length' | awk '{print $2}')

echo "$SIZE"
