#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0: 
    lastNum = number % 10
elif number <= 0:
    lastNum = number % -10
print('Last digit of {:d} is {:d}'. format(number, lastNum), end=" ")
if lastNum > 5:
    print('and is greater than 5')
elif lastNum == 0:
    print('and is 0')
elif lastNum < 6:
    print('and is less than 6 and not 0')
