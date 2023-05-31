#!/usr/bin/python3
# 0-square.py
"""A module that defines a square."""


class Square:
    """Define a square."""

    def __init__(self, size=0):
        """Initialise method.

        Args:
            size (int): Sqaure size.

        Raises:
            TypeError: If type is not int instance.
            ValueError: If `size` < 0.

        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the current square area.

        Returns:
            int: Area of a square

        """
        return (self.__size * self.__size)
