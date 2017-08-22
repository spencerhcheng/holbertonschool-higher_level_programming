#!/bin/bash
# Sends a POST request to the URL with the specified key and variable names
curl -F "email=hr@holbertonschool.com" -F "subject=I will always be here for PLD" "$1"
