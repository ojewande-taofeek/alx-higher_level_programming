#!/usr/bin/python3
def islower(c):
    # returns True if c is lower else False
    value = ord(c)
    if value >= 97 and value <= 122:
        return True
    else:
        return False
