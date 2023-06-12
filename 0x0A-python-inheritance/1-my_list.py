#!/usr/bin/python3


class MyList(list):
    """Class that inherits from list."""

    def __init__(self):
        """Initialise."""
        self.list = list

    def print_sorted(self):
        """Print sorted list."""
        print(sorted(self))
