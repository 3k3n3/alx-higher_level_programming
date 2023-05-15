#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for line in matrix:
        for i in line:
            print("{:d}{}".format(i, " " if l.index(i) != len(l) - 1
                                  else ""), end="")
        print("")
