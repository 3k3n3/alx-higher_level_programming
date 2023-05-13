#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list."""
    if idx < 0 and idx > len(my_list):
        return None
    return(my_list[idx])
