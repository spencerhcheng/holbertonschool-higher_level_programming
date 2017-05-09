#!/usr/bin/python3
def no_c(my_string):
    str_cpy = ""
    for i in range(len(my_string)):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            continue
        else:
            str_cpy = str_cpy + my_string[i]
    return str_cpy
