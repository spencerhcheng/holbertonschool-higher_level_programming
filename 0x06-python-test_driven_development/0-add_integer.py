#!/usr/bin/python3
def add_integer(a, b):
    if isinstance(a, float) or isinstance(a, int):
        if isinstance(b, float) or isinstance(b, int):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
