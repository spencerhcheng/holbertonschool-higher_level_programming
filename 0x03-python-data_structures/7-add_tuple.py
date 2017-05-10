#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_list = list(tuple_a)
    b_list = list(tuple_b)

    if len(a_list) < 2:
        for i in range(2):
            a_list.append(0)
    if len(b_list) < 2:
        for i in range(2):
            b_list.append(0)

    sumA = a_list[0] + b_list[0]
    sumB = a_list[1] + b_list[1]

    result_tuple = (sumA, sumB)
    return (result_tuple)
