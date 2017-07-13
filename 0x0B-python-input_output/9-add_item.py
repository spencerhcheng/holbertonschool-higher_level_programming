#!/usr/bin/python3
import json
import sys
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

argc = len(sys.argv)

filename = "add_item.json"
super_list = []
"""
If file doesn't exist, create it and add empty list
"""
if not os.path.exists("./add_item.json"):
    save_to_json_file(super_list, filename)

"""
Load contents from file add_item.json and store in list
"""
super_list = load_from_json_file(filename)

"""
Append new elements to existing list from add-item.json
"""
for i in range(1, argc):
    super_list.append(sys.argv[i])
"""
Overwrite add-item.json contents with newly appended super_list list
"""
save_to_json_file(super_list, filename)
