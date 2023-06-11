#!/usr/bin/python3


class MyList(list):
    """Class that inherits from list."""

    def __init__(self):
        self.list = list

    def print_sorted(self):
        print(sorted(self))
