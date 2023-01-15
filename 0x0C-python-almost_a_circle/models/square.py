#!/usr/bin/python3
"""

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__width)

    @property
    def size(self):
        return self.__height

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("Width must be an integer")
        if size <= 0:
            raise ValueError("Width must be > 0")
        self.__width = size
        self.__height = size

    def update(self, *args, **kwargs):
        atts = ["id", "size", "x", "y"]
        [setattr(self, a, b) for a, b in zip(atts, args)]
        [setattr(self, a, b) for a, b in kwargs.items()]
