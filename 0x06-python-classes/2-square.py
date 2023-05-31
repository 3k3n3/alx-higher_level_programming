#!/usr/bin/python3
"""Define square."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialise method.

        Args:
            size (int): Square size.

        Raises:
            TypeError: If type is not int instance
            ValueError: If `size` < 0.

        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
