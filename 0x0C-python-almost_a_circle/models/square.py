#!/usr/bin/python3
"""define a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """reprsent square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
        self.__x = x
        self.__y = y

    def __str__(self):
            return ("[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.size))
    
    @property
    def size(self):
        return self.__width
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def size(self):
        return self.__height
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def update(self, *args, **kwargs):
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
