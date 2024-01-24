#!/usr/bin/python3

"""Define a class."""


class Square:
    """Represent the square."""

    def __init__(self, size=0):
        """Initialize the Square instance with size.

        Args:
            size (int): The size of the square.
        """

        self.__size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print('#' * self.size)
