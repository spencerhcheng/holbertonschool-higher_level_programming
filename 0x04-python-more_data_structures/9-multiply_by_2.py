#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = my_dict.copy()
    for key, val in new_dict.items():
        new_dict[key] = val * 2
    return new_dict
