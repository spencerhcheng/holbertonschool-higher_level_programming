#!/bin/bash
# Sends a POST request to the URL with the specified key and variable names
curl -sd "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
