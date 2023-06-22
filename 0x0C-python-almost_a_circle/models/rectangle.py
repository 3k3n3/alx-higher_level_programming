#!/usr/bin/python3
"""Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor."""
        self.get_width(width)
        self.get_height(height)
        self.get_x(x)
        self.get_y(y)
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
                    self.get_width(value)
                elif key == "height":
                    self.get_height(value)
                elif key == "x":
                    self.get_x(value)
                elif key == "y":
                    self.get_y(value)

    @property
    def get_width(self):
        """Public getter."""
        return self.__width

    @get_width.setter
    def get_width(self, value):
        """Public setter for width."""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def get_height(self):
        """Public getter."""
        return self.__height

    @get_height.setter
    def get_height(self, value):
        """Public setter for height."""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def get_x(self):
        """Public getter."""
        return self.__x

    @get_x.setter
    def get_x(self, value):
        """Public setter for x."""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def get_y(self):
        """Public getter."""
        return self.__y

    @get_y.setter
    def get_y(self, value):
        """Public setter for y."""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """String representation."""
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
