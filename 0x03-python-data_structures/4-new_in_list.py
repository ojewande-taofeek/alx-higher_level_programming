#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ function that replaces an element in a list at a
        specific position without modifying the original list (like in C)
    """
    if not my_list or idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
