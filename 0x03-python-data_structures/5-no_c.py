#!/usr/bin/python3
def no_c(my_string):
    """Removes chars 'c' and 'C'."""
    str_list = [i for i in my_string]
    for enum, char in enumerate(str_list):
        if char in "cC":
            str_list.pop(enum)
    return "".join(str_list)
