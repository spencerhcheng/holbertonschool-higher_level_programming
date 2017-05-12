#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0

    my_dict = dict(my_list)

    list_product = 0
    list_sum = 0

    for k, v in my_dict.items():
        list_product = list_product + (k * v)
        list_sum = list_sum + v

    return (list_product / list_sum)
