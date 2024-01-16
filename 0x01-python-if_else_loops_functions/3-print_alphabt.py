#!/usr/bin/python3
letters = 97
while letters <= 122:
    if letters == 113 or letters == 101:
        pass
    else:
        print("{:c}".format(letters), end="")
    letters = letters + 1
