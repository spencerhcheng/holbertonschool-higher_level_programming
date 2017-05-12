#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    set_combo = set_1.union(set_2)
    for x in set_combo:
        for y in set_1:
            for z in set_2:
                if z == y and y == x:
                    uniq = z
                    set_combo.remove(uniq)
                    return set_combo
