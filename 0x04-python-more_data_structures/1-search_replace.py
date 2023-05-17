#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    return [i if i != search else replace for i in my_list]
