#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # function that prints x elements of a list
    try:
        counter = 0
        for mem in my_list:
            if counter < x:
                print(mem, end="")
                counter += 1
    except ValueError:
        pass
    print()
    return counter
