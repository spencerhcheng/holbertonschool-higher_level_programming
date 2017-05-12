#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_combo = set_1.union(set_2)
    for x in set_combo:
        for y in set_1:
            for z in set_2:
                if z == y and y == x:
                    return(z)
