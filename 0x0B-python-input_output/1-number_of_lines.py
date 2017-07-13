#!/usr/bin/python3


def number_of_lines(filename=""):
    """ Prints to standard output, the number of lines in file """
    with open(filename, encoding='utf-8') as file_open:
        line_count = 0
        for line in file_open:
            line_count += 1
        return (line_count)
