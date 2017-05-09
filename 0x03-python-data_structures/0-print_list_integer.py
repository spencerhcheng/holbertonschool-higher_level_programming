#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = len(my_list)
    j = 0
    while j < i:
        print ("{:d}".format(my_list[j]))
        j = j + 1
