#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        return self.__size 

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        if isinstance(self.__size, int):
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                return int(self.__size) ** 2
        else:
            raise TypeError("size must be an integer")
