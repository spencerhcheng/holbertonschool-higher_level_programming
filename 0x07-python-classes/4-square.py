#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        if isinstance(self.__size, int):
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                return self.__size
        else:
            raise TypeError("size must be an integer")

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        if isinstance(self.__size, int):
            return int(self.__size) ** 2
