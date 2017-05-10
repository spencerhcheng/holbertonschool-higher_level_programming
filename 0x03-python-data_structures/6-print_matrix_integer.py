#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None or matrix != [[]]:
        for x in matrix:
            for (i, val) in enumerate(x):
                if i < len(x) - 1:
                    print("{:d} ".format(val), end="")
                else:
                    print("{:d}".format(val))
