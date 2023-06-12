#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square properties."""

    def __init__(self, size):
        """Initialize Square

        Args:
            size: represents the size of the square defined

        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area of square."""
        return self.__size**2
