#!/usr/bin/python3
"""A function that appends a str at the end of a text file (UTF8)
and returns num of chars added."""


def append_write(filename="", text=""):
    """Append to file and return num of chars added."""
    with open(filename, "a") as f:
        return f.write(text)
