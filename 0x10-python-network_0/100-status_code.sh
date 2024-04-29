#!/bin/bash

#send request, pass arguement, and display
curl -s -o /dev/null -w "%{http_code}" "$1"
