#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for line in matrix:
        for i in line:
            print("{:d}{}".format(i, " " if line.index(i) != len(line) - 1
                                  else ""), end="")
        print("")
