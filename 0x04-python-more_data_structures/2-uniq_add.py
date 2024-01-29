#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ function that adds all unique integers
        in a list (only once for each integer)
    """
    add = 0
    if my_list:
        for x in set(my_list):
            add += x
    return add
