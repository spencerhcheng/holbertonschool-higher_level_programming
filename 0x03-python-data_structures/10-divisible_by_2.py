#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    if my_list is not None:
        new_list = []
        for i, val in enumerate(my_list):
            if val % 2 == 0:
                new_list.append(True)
            elif val % 2 != 0:
                new_list.append(False)
    return new_list
