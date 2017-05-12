#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    new_dict = my_dict.copy()
    add_key = 0
    for k, val in my_dict.items():
        if k == key:
            my_dict[k] = value
        if key != k:
            add_key = 1
        else:
            continue
    if add_key == 1:
        my_dict[key] = value
    return my_dict
