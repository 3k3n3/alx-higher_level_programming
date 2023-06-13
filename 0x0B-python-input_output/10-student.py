#!/usr/bin/python3
"""A class Student that defines a student."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Instantiante method."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dict representation of student."""
        if attrs is not None:
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
