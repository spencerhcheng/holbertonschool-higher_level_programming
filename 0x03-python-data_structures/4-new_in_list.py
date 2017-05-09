#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    list_cpy = my_list[:]
    if idx > len(my_list):
        return my_list

    else:
        list_cpy[idx] = element
        return list_cpy
