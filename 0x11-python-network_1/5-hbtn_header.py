#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    """
    Prints out X-Request-Id header
    """
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
