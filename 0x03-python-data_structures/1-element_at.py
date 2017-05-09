def element_at(my_list, idx):
    str_len = len(my_list)
    if idx > str_len:
        return (None)

    return("{:d}".format(my_list[idx]))
