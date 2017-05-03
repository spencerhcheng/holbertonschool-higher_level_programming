#!/usr/bin/python3
def remove_char_at(str, n):
    x = len(str)
    if n < 0:
        return(str)
    else:
        str = str[0:n] + str[n + 1:x]
        return(str)
