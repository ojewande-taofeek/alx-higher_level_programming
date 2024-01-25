#!/usr/bin/python3
def max_integer(my_list=[]):
    # function that finds the biggest integer of a list.
    if my_list:
        biggest = my_list[0]
        for num in my_list:
            if biggest < num:
                biggest = num
        return biggest
    return None
