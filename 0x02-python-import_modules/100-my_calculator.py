#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    num_of_args = len(argv) - 1
    if num_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = argv[2]
    first = int(argv[1])
    second = int(argv[3])
    if op == "+":
        print("{} {} {} = {}".format(first, op, second, add(first, second)))
    elif op == "-":
        print("{} {} {} = {}".format(first, op, second, sub(first, second)))
    elif op == "*":
        print("{} {} {} = {}".format(first, op, second, mul(first, second)))
    elif op == "/":
        print("{} {} {} = {}".format(first, op, second, div(first, second)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
