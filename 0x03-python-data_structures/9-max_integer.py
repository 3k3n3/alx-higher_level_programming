#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns biggest integer w/out using max()."""
    return sorted(my_list)[-1] if len(my_list) > 0 else None
