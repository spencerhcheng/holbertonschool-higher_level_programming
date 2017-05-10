#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if idx <= 0 or idx >= len(my_list):
        return my_list
    else:
        for i, ele in enumerate(my_list):
            if i == idx:
                del my_list[idx]
            else:
                my_list[i] = ele
        return my_list
