#!/usr/bin/python3
"""Base class."""
import json


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instatiate class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Convert to json."""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file."""
        if list_objs is None:
            list_objs = []
        file = f"{cls.__name__}.json"

        with open(file, "w") as f:
            f.write(cls.to_json_string([i.to_dictionary() for i in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns JSON string representation."""
        if json_string is None:
            json_string = []
        return json_string

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError("Invalid class name")
        dummy_instance.update(
            **dictionary
        )  # Apply the real values using the update method
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        file = f"{cls.__name__}.json"
        try:
            with open(file) as f:
                json_data = f.read()
        except FileNotFoundError():
            return []
        instances = [cls.create(**i) for i in json.loads(json_data)]
        return instances
