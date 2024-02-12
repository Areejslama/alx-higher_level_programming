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
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square"""
        if args and len(args) != 0:
            if len(args) >= 1:
                if not isinstance(args[0], int) and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
                if len(args) > 2:
                    self.size = args[1]
                if len(args) > 3:
                    self.__x = args[2]
                if len(args) > 4:
                    self.__y = args[3]
        for key, value in kwargs.items():
            if key == 'id':
                if not isinstance(value, int) and value is not None:
                    raise TypeError("id must be an int")
                self.id = value
            elif key == 'size':
                self.size = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value


    def to_dictionary(self):
        """Return the dictionary representation of the rectangle"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.__x,
            'y': self.__y
            }
