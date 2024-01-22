#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    else:
        args_num = len(argv) - 1
        if args_num == 1:
            print("{} argument:".format(args_num))
        else:
            print("{} arguments:".format(args_num))
        for args_index in range(1, len(argv)):
            print("{}: {}".format(args_index, argv[args_index]))
""" args_index = 1
    while args_num > 0:
    print("{}: {}".format(args_num, argv(args_index)))
    args_num = args_num - 1
"""
