#!/usr/bin/python3
"""Base class."""
import json
import csv
import turtle


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
            with open(file, "r") as f:
                json_data = f.read()
        except FileNotFoundError():
            return []
        instances = [cls.create(**i) for i in cls.from_json_string(json_data)]
        return instances


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize and save instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize and load instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(
                            id=int(row[0]),
                            width=int(row[1]),
                            height=int(row[2]),
                            x=int(row[3]),
                            y=int(row[4]),
                        )
                    elif cls.__name__ == "Square":
                        instance = cls.create(
                            id=int(row[0]),
                            size=int(row[1]),
                            x=int(row[2]),
                            y=int(row[3]),
                        )
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw shapw with turtle."""
        win = turtle.Screen()
        win.bgcolor("light blue")
        win.title("ALX Turtle GUI")
        draw = turtle.Turtle()

        for obj in list_rectangles:
            draw.penup()
            draw.goto(obj.get_x(), obj.get_y())
            draw.pendown()
            draw.begin_fill()
            for i in range(2):
                draw.color("blue")
                draw.forward(obj.get_width())
                draw.right(90)
                draw.forward(obj.get_height())
                draw.right(90)
                draw.fillcolor("white")
            draw.end_fill()

        for obj in list_squares:
            draw.penup()
            draw.goto(obj.get_x(), obj.get_y())
            draw.pendown()
            draw.begin_fill()
            for i in range(4):
                draw.color("green")
                draw.forward(obj.get_width())
                draw.right(90)
                draw.fillcolor("yellow")
            draw.end_fill()

        turtle.done()
