#!/bin/bash
# Displays the size of the body of the response
curl -sI "$1" | grep Allow | cut -d ":" -f2 | sed -e 's/^[ \t]*//'
