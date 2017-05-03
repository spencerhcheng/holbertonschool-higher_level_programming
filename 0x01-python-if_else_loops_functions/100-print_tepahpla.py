#!/usr/bin/python3
x = 122

while (x > 96):
    temp = x
    if (x % 2 != 0):
        temp = x - 32
    print('{}'.format(chr(temp)), end="")
    x = x - 1
