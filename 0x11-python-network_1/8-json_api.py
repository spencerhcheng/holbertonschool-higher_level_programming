#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    dic = {}
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        dic['q'] = ""
    elif len(sys.argv) == 2:
        dic['q'] = sys.argv[1]

    r = requests.post(url, dic)
    try:
        json_rep = r.json()
        if bool(json_rep) is False:
            print("No result")
        else:
            print("[{}] {}".format(json_rep['id'], json_rep['name']))
    except:
        print("Not a valid JSON")
