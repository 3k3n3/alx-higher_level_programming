#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    points = 0
    total_weight = 0
    for i in my_list:
        points += i[0] * i[1]
        total_weight += i[1]
    return points / total_weight
