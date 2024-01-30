#!/usr/bin/python3
def weight_average(my_list=[]):
    """  function that returns the weighted
        average of all integers tuple (<score>, <weight>)
    """
    total_mark = 0
    weight = 0
    total_weight = 0
    if my_list:
        for a in my_list:
            each_mark = a[0] * a[1]
            total_mark += each_mark
            total_weight += a[1]
        weight = total_mark / total_weight
        return weight
    return weight
