#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """represent a geometry base class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """represent a rectangle"""
    def __init__(self, width, height):
        """instant of rectangle"""
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """represent a string"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    """represent a square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
