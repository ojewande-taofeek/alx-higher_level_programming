#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    addition = 0
    for num in range(1, len(argv)):
        addition = addition + int(argv[num])
    print("{}".format(addition))
