#!/usr/bin/python3
import json


def class_to_json(obj):
    """
    Returns the dictionary description with simple
    data structure for JSON serialization of an object
    """
    serialized = json.dumps(obj.__dict__)
    return(json.loads(serialized))
