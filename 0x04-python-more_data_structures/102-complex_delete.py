#!/usr/bin/python3
def complex_delete(my_dict, value):
    
    dict_vals = list(my_dict.values())
    dict_keys = list(my_dict.keys())

    for i, ele in enumerate(dict_vals):
        if ele == value:
            del dict_vals[i]
            del dict_keys[i]

    new_dict = dict(zip(dict_keys, dict_vals))
 
    return new_dict
