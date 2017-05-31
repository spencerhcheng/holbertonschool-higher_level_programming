#!/usr/bin/python3
class MyList(list):
    new_list = []

    def print_sorted(self):
        self.new_list.append(self)
        for x in self.new_list:
            print(sorted(x))
