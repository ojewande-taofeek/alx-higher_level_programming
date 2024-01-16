#!/usr/bin/python3
for first in range(9):
    for second in range(1, 10):
        if first == 8 and second == 9:
            print("{}{}".format(first, second))
            break
        elif first >= second:
            continue
        else:
            print("{}{}".format(first, second), end=", ")
