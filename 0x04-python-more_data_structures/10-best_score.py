#!/usr/bin/python3
def best_score(my_dict):
    if my_dict == None:
        return None

    dict_list = list(my_dict.values())
    
    for sum_of_num in dict_list:
        sum_of_num += sum_of_num

    if sum_of_num == 0:
        return None

    max = dict_list[0]

    for key, val in my_dict.items():
        if my_dict[key] > max:
            max = my_dict[key]
            if val == max:
                return key
