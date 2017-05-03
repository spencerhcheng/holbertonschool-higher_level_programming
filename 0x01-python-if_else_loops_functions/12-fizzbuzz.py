#!/usr/bin/python3
def fizzbuzz():
    num = 1

    while num < 101:
        if num % 3 == 0 and num % 5 != 0:
            print("Fizz ", end="")
        elif num % 3 != 0 and num % 5 == 0:
            print("Buzz ", end="")
        elif num % 15 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{:d} ".format(num), end="")
        num = num + 1
