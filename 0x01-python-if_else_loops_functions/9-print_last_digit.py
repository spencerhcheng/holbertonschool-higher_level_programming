#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print('{:d}'.format(number % 10), end="")
    elif number < 0:
        number = number * -1
        print('{:d}'.format(number % 10), end="")
