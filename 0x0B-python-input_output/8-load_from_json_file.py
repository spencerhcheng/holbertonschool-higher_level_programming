#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as file_open:
        f = json.load(file_open)
        return(f)
