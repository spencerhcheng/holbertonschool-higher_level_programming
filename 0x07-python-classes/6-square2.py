#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0,0)):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if not all(isinstance(x, int)) for x in position or x in position < 0:
            raise TypeError("position must be a tuple of 2 positive numbers")
        else:
            self.__position = position
 
    @property
    def size(self):
        return self.__size 

    @size.setter
    def size(self, value):
        self.__size = value

    @prop.position
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        if isinstance(self.__size, int):
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                return int(self.__size) ** 2
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        if self.__size == 0:
            print('')
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print("")
