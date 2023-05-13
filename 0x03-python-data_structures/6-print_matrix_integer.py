#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for l in matrix:
        for i in l:
            print("{:d}{}".format(i, " " if l.index(i) != len(l) - 1
                                  else ""), end="")
        print()
