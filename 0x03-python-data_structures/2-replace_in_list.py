#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace list element at index."""
    if idx < 0:
        return my_list
    if len(my_list) == 0:
        return (my_list)
    if idx > len(my_list):
        return my_list
    my_list.pop(idx)
    my_list.insert(idx, element)
    return my_list
