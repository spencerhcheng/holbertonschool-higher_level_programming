#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(-17)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))
