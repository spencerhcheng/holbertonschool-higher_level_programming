#!/usr/bin/python3


def write_file(filename="", text=""):
    """
    writes a string to a text file
    and returns the number of chars
    written
    """
    with open(filename, mode='w', encoding='utf-8') as file_open:
        return file_open.write(text)
