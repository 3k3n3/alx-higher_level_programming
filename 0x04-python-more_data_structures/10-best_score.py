#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    a_dict = a_dictionary
    if a_dict is not None:
        max_value = sorted(list(a_dict.values()))[-1]
        return "".join({i for i in a_dict if a_dict[i] == max_value})
