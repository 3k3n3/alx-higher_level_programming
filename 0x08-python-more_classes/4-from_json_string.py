# !/usr/bin/python3
"""A function that returns an object (Python data structure)
represented by a JSON string."""
import json


def from_json_string(my_str):
    """Returns the Python object of a JSON string."""
    return json.loads(my_str)
