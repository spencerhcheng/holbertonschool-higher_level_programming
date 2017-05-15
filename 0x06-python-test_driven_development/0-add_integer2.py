#!/usr/bin/python3
def add_integer(a, b):
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    result = True
    while (result is True):
        try:
            if a == True or a == False:
                raise TypeError('a must be an integer')
            a + 0
        except TypeError:
            result = False
            return('a must be an integer')
        try:
            if b == True or b == False:
                raise TypeError('b must be an integer')
            b + 0
        except TypeError:
            result = False
            return('b must be an integer')
        
        finally:
            if result is True:
                return (a + b)
