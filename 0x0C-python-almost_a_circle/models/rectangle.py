#!/usr/bin/python3
"""

"""
import sys

from base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("Width must be an integer")
        if width <= 0:
            raise ValueError("Width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("Height must be an integer")
        if height <= 0:
            raise ValueError("Height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for y in range(self.__y):
            print()
        for height in range(self.__height):
            print(" " * self.__x, '#' * self.__width)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        atts = ["id", "width", "height", "x", "y"]
        [setattr(self, a, b) for a, b in zip(atts, args)]
        [setattr(self, a, b) for a, b in kwargs.items()]


r1 = Rectangle(10, 10, 10, 10)
print(r1)

r1.update(height=1)
print(r1)

r1.update(width=1, x=2)
print(r1)

r1.update(y=1, width=2, x=3, id=89)
print(r1)

r1.update(x=1, height=2, y=3, width=4)
print(r1)
