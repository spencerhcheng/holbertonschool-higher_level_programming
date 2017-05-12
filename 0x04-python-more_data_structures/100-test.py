#!/usr/bin/python3

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]

my_dict = dict(my_list)

list_product = 0
list_sum = 0

for k, v in my_dict.items():
    list_product = list_product + (k * v)
    list_sum = list_sum + v
    
print(list_product)
print(list_sum)
print (list_product / list_sum)

