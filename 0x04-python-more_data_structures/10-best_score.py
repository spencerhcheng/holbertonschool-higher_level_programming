#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None

    dict_list = list(my_dict.values())

    max = dict_list[0]

    for key, val in my_dict.items():
        if val > max:
            max = val
            if val == max:
                return key
