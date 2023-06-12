#!/usr/bin/python3
"""Is kind of class."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class.

    or if obj is an instance of a class that inherited from a_class.
    """
    return isinstance(obj, a_class)
