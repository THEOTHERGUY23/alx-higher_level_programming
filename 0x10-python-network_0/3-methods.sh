#!/bin/bash

#Display all http methods accepted by server

curl -sI "$1" | grep "Allow" | cut -d " " -f2-
