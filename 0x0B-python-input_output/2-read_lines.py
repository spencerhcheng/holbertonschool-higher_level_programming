#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """ reads n lines of text file and prints it to standard out """
    line_c = 0
    with open(filename, encoding='utf-8') as file_open:
        line_c = sum(1 for count in file_open)
        file_open.seek(0)
        if not nb_lines <= 0 or nb_lines >= line_c:
            while nb_lines > 0:
                print(file_open.readline(), end="")
                nb_lines -= 1
        else:
            for x in file_open:
                print(x, end="")
