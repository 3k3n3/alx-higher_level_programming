#!/usr/bin/python3
"""Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class."""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """String representation."""
        id = self.id
        x = self.get_x()
        y = self.get_y()
        return f"[Square] ({id}) {x}/{y} - {self.get_height()}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.get_x(),
            "y": self.get_y(),
        }

    @property
    def size(self):
        """Get size."""
        return self.get_width()

    @size.setter
    def size(self, size):
        """Set size."""
        self.set_width(size)
        self.set_height(size)
