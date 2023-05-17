#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    new_matrix = []
    for row in matrix:
        new_row = []
        new_matrix.append(new_row)
        for i in row:
            new_row.append(i * i)
    return new_matrix
