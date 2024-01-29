#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # function that computes the square value of all integers of a matrix
    if matrix:
        return [[x**2 for x in row] for row in matrix]


"""
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(x**2)
        new_matrix.append(new_row)
    return new_matrix
"""
