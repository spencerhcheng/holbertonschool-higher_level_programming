#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {}
    email['email'] = sys.argv[2]

    r = requests.post(url, email)
    print(r.content.decode('utf-8'))
