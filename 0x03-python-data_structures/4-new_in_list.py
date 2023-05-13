#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace element in list."""
    if idx < 0:
        return my_list
    if len(my_list) == 0:
        return my_list
    if idx > len(my_list):
        return my_list
    new_list = [i for i in my_list]
    new_list.pop(idx)
    new_list.insert(idx, element)
    return new_list
