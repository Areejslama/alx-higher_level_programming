#!/usr/bin/python3
"""define a square class"""

from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """represent square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Get the size of the square"""
        return self.__width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square"""
        if len(args) >= 1:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if len(args) >= 2:
            self.size = args[1]
        elif 'size' in kwargs:
            self.size = kwargs['size']
        if len(args) >= 3:
            self.__x = args[2]
        elif 'x' in kwargs:
            self.__x = kwargs['x']
        if len(args) >= 4:
            self.__y = args[3]
        elif 'y' in kwargs:
            self.__y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.__x,
            'y': self.__y
            }
