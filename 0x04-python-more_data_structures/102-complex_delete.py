#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for i in a_dictionary:
            if a_dictionary[i] == value:
                del a_dictionary[i]
                break
    return a_dictionary
