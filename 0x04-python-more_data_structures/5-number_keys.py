#!/usr/bin/python3
def number_keys(my_dict):
    my_list = list(my_dict.values())
    count = 0
    for i in my_list:
        count += 1
    return count
