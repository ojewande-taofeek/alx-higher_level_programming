#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # function that prints a dictionary by ordered keys.
    key_list = sorted(a_dictionary)
    for k in key_list:
        for keys, values in a_dictionary.items():
            if k == keys:
                print("{}: {}".format(keys, values))
