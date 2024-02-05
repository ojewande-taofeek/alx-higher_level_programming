#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # function that prints the first x elements of a list and only integers
    counter = 0
    if my_list:
        for mem in my_list:
            try:
                if counter < x:
                    print("{:d}".format(mem), end="")
                    counter += 1
            except Exception:
                pass
    print()
    return counter
