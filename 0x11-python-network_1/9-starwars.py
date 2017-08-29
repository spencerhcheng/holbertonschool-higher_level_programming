#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    search_param = sys.argv[1]
    url = 'https://swapi.co/api/people/?search={}'.format(search_param)
    count = 0
    r = requests.get(url)
    response_obj = r.json()

    print("Number of result: {}".format(response_obj['count']))

    results = response_obj['results']
    for person in results:
        print(person['name'])
