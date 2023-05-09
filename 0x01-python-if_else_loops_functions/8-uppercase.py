#!/usr/bin/python3
def uppercase(str):
    """Converts str to upper case."""
    new_str = ""
    for c in str:
        if ord(c) in range(97, 123):
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
    print(new_str)
