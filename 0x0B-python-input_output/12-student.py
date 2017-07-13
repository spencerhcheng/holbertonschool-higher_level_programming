#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Create public instance attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve only attributes contained in class
        """
        partial_dict = {}
        if attrs is not None:
            for x in range(len(attrs)):
                try:
                    f = getattr(self, attrs[x])
                    partial_dict[attrs[x]] = f
                except:
                    pass
            return partial_dict
        else:
            return self.__dict__
