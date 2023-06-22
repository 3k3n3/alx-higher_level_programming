#!/usr/bin/python3
"""Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor."""
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)
        super().__init__(id=id)

    def area(self):
        """Calculate area of a rectangle."""
        return self.get_height() * self.get_width()

    def display(self):
        """Prints the Rectangle instance with '#'."""
        for i in range(self.get_y()):
            print()
        for i in range(self.get_height()):
            print(" " * self.get_x() + "#" * self.get_width())

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if len(args) > 0:
            self.id = args[0]
        # Skip the id argument if present
        if args:
            args = args[1:]
        if kwargs:
            for key, value in kwargs.items():
                if key == "width":
                    self.set_width(value)
                elif key == "height":
                    self.set_height(value)
                elif key == "x":
                    self.set_x(value)
                elif key == "y":
                    self.set_y(value)

    def get_width(self):
        """Public getter."""
        return self.__width

    def set_width(self, width):
        """Public setter for width."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    def get_height(self):
        """Public getter."""
        return self.__height

    def set_height(self, height):
        """Public setter for height."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def get_x(self):
        """Public getter."""
        return self.__x

    def set_x(self, x):
        """Public setter for x."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    def get_y(self):
        """Public getter."""
        return self.__y

    def set_y(self, y):
        """Public setter for y."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    # def __str__(self):
    #     """String representation."""
    #         return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
    # {self.__width}/{self.__height}"

    def __str__(self):
        """Defines a format for the string representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
