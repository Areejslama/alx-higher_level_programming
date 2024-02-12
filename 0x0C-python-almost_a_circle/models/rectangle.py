#!/usr/bin/python3
"""define a base class"""


from models.base import Base


class Rectangle(Base):
    """represent subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ set x of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set y of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__height):
            print('#' * (self.__width))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y,
            self.width, self.height)

    def display(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        if len(args) >= 1:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if len(args) >= 2:
            self.__width = args[1]
        elif 'width' in kwargs:
            self.__width = kwargs['width']
        if len(args) >= 3:
            self.__height = args[2]
        elif 'height' in kwargs:
            self.__height = kwargs['height']
        if len(args) >= 4:
            self.__x = args[3]
        elif 'x' in kwargs:
            self.__x = kwargs['x']
        if len(args) >= 5:
            self.__y = args[4]
        elif 'y' in kwargs:
            self.__y = kwargs['y']

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.__x,
            'y': self.__y,
            }
