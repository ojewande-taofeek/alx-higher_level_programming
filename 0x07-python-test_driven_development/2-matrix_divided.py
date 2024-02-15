#!/usr/bin/python3
"""Contains a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
        function that divides all elements of a matrix
        Args:
            matrix: nested list containing only int
            div: the divisor of type int
        Returns:
            A new matrix containing divided elements
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = list()
    for row in matrix:
        row_list = list()
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix " + "(list of lists)"
                                + " of integers/floats")
            row_list.append(round(element / div, 2))
        new_list.append(row_list)
    return new_list
