#!/usr/bin/python3


def read_file(filename=""):
    """ Opens file and prints to std out """
    with open(filename, encoding='utf-8') as file_open:
        for line in file_open:
            print(line, end="")
