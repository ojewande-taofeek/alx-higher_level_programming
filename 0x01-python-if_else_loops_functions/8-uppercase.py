#!/usr/bin/python3
def uppercase(str):
    # function that prints a string in uppercase followed by a new line
    for i in str:
        value = ord(i)
        if value >= 97 and value <= 122:
            i = chr(value - 32)
        print("{:}".format(i), end="")
    print()
