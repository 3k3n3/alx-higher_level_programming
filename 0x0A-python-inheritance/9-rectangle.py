#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle properties."""

    def __init__(self, width, height):
        """Initializing this Rectangle class

        Args:
            width: represents the rect width
            height: represents the rect height

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Str representation."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
