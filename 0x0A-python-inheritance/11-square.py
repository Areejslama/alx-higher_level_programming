#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        """Placeholder area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        """Initialize the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class representing a square, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
