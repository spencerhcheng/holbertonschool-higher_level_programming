#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor with width, height, x, y, id attr
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Setter method for width
        """
        self.__width = width

    @property
    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter method for height
        """
        self.__height = height

    @property
    def x(self):
        """
        Getter method for x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Setter method for y
        """
        self.__x = x

    @property
    def y(self):
        """
        Getter method for y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Setter method for y
        """
        self.__y = y
