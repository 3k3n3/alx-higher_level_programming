#!/usr/bin/python3


def inherits_from(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class

    that inherited (directly or indirectly) from the specified class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
