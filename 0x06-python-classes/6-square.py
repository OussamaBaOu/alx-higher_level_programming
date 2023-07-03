#!/usr/bin/python3
"""Define class Square."""


class Square:
    """Represent square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new square.

        Args:
            size (int): The size of new square.
            position (int, int): The position of new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for c in range(0, self.__size)]
            print("")