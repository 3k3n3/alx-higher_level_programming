#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """A function that executes a function safely."""
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", str(e), file=sys.stderr)
