#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Reads and prints a text file."""
    with open(filename) as f:
        print(f.read(), end="")
