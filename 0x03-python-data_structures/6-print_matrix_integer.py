#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # function that prints a matrix of integers
    if matrix:
        for row in matrix:
            for num in range(len(row)):
                if num == len(row) - 1:
                    print("{:d}".format(row[num]), end="")
                else:
                    print("{:d}".format(row[num]), end=" ")
            print()
