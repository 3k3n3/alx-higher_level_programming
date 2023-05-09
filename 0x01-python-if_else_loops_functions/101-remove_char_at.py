#!/usr/bin/python
def remove_char_at(str, n):
    """Remove str char at n"""
    if n < len(str) and n >= 0:
        str = str.replace(str[n], "")
    return(str)