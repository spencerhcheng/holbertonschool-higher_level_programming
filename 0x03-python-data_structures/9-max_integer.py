#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0

    if my_list is not None:
        for i, val in enumerate(my_list):
            if val > max:
                max = val
    return max
