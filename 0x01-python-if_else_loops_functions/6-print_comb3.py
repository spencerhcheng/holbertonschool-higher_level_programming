#!/usr/bin/python3

for num1 in range(10):
    for num2 in range(1 + num1, 10):
        if num1 == 8 and num2 == 9:
            print("{:d}".format(89))
        else:
            print('{:d}{:d}'.format(num1, num2), end=", ")
