#!/usr/bin/python3
def uppercase(str):

    for c in str:
        char = ord(c)
        if char > 96 and char < 123:
            char = char - 32
        print('{:c}'.format(char), end="")
    print("")
