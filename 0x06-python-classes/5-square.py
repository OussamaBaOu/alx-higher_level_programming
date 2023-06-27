#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Represent square."""

    def __init__(self, size):
        """Initialize new square.

        Args:
            size (int): The size of new square.
        """
        self.size = size

    def size(self):
        """Get/set the current size of square."""
        return (self.__size)

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
