#!/usr/bin/python3
"""A function that writes a string to a text file (UTF8)
and returns the number of characters."""


def write_file(filename="", text=""):
    """Write to file and return num of chars."""
    with open(filename, "w") as f:
        return f.write(text)
