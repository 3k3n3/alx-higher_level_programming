#!/usr/bin/python3


def add_attribute(obj, attr_name, attr_value):
    """Add atrribute

    Check if the object has the '__dict__' attribute

    Args:
        obj: object
        attr_name: name/key
        atrr_value: value

    Raises:
        TypeError: if object does not have '__dict__' attribute
            and can't be added

    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
