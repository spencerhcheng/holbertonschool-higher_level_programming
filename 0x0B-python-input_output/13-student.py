#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Instantiate public attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves only attributes contained in class
        """
        partial_dict = {}
        if attrs is not None:
            for x in range(len(attrs)):
                try:
                    attributes = getattr(self, attrs[x])
                    partial_dict[attrs[x]] = attributes
                except:
                    pass
            return partial_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attrs of the Student instance
        """
        attrs_list = ["first_name", "last_name", "age"]
        if attrs_list[0] in json:
            self.first_name = json[attrs_list[0]]
        if attrs_list[1] in json:
            self.last_name = json[attrs_list[1]]
        if attrs_list[2] in json:
            self.age = json[attrs_list[2]]
