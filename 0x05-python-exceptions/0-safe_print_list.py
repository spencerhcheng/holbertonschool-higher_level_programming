#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        strlen = 0
        for i in my_list:
            strlen += 1
        if x <= strlen:
            for i in range(x):
                print('{:d}'.format(my_list[i]), end="")
            print()
            return x
        else:
            for i in range(strlen):
                print('{:d}'.format(my_list[i]), end="")
            print()
            return strlen
    except (TypeError, NameError):
        pass
