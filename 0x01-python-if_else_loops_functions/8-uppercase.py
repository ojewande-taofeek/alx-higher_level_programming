#!/usr/bin/python3
def uppercase(str):
    for i in str:
        value = ord(i)
        if value >= 97 and value <= 122:
            i = chr(value - 32)
        print("{:}".format(i), end="")
    print()
