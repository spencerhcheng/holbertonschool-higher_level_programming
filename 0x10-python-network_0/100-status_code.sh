#!/bin/bash
# Displays HTTP status code of cURL response
curl -so /dev/null -Iw "%{http_code}" "$1"
