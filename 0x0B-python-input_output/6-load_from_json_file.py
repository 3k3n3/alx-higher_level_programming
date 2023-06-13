#!/usr/bin/python3
"""A function that creates an Object from a “JSON file"."""
import json


def load_from_json_file(filename):
    """Creates object from JSON file."""
    with open(filename) as f:
        return json.load(f)
