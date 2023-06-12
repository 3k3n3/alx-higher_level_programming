#!/usr/bin/python3


class BaseGeometry:
    """Base Geometry."""

    def area(self):
        """Calculates area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer

        Args:
            name: name of object

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
