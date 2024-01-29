#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ function that replaces all occurrences of an element
        by another in a new list
    """
    if my_list:
        new_list = []
        for x in my_list:
            if x == search:
                x = replace
            new_list.append(x)
        return new_list


# return [x if x != search else replace for x in my_list]
