#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0

    for i in range(x):
        try:
            length += 1
            print('{:d}'.format(my_list[i]), end="")
        except (TypeError, ValueError):
            length -= 1
    print()
    return length
