#!/usr/bin/python3
def no_c(my_string):
    # function that removes all characters c and C from a string
    if my_string:
        new_str = str()
        for char in my_string:
            if char == 'c' or char == 'C':
                pass
            else:
                new_str = new_str + char
        return new_str
