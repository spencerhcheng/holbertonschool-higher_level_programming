#!/usr/bin/python3
num1 = 1
num2 = 1

while num1 < 10 and num1 != num2:
    print('{:d}'.format(num1), end="")
    num1 = num1 + 1
    while num2 < 10 and num2 != num1:
        print('{:d}'.format(num2), end="")
        num2 = num2 + 1
