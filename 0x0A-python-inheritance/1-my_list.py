#!/usr/bin/python3
"""Class MyList."""


class MyList(list):
    """Class that inherits from list."""

    def print_sorted(self):
        """Print sorted list."""
        print(sorted(self))
