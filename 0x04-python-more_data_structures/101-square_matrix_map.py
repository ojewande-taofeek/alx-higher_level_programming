#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (map((lambda x: x * 2, x for x in row) for row in matrix))
