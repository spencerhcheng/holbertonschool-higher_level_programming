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
        for film in person['films']:
            rf = requests.get(film)
            rf_obj = rf.json()
            print("\t{}".format(rf_obj['title']))

    next_page = response_obj['next']
    while next_page is not None:
        r = requests.get(next_page)
        response_obj = r.json()
        results = response_obj['results']
        for person in results:
            print(person['name'])
            for film in person['films']:
                rf = requests.get(film)
                rf_obj = rf.json()
                print("\t{}".format(rf_obj['title']))
        next_page = response_obj['next']
        if next_page is None:
            break
