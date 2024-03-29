#!/usr/bin/python3
"""Defines square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new Square.

        Args:
            size (int): size of new Square.
            x (int): x coordinate of new Square.
            y (int): y coordinate of new Square.
            id (int): identity of new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square.

        Args:
            *args (ints): attribute values.
                - 1st argument represents id
                - 2nd argument represents size
                - 3rd argument represents x
                - 4th argument represents y
            **kwargs (dict): New value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
