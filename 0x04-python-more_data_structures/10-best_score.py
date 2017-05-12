#!/usr/bin/python3
def best_score(my_dict):

    if my_dict is None:
        return None

    dict_list = list(my_dict.values())

    for key, val in my_dict.items():
        if val == max(dict_list):
            return key
