#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs != None:
            for x in range(len(attrs)):
                try:
                    f = getattr(self, attrs[x])
                    return json.dumps(f)
                except:
                    pass
        else:
            f = json.dumps(self.__dict__)
            return json.loads(f)

