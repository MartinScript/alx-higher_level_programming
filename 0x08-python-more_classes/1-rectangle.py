#!/usr/bin/python3
"""
A Rectangle
"""


class Rectangle:
    """
    functions and data
    """
    def __init__(self, width=0, height=0):
        """instantiation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            """width must be an integer"""
            raise TypeError("width must be an integer")
        if value < 0:
            """width must be greater than 0"""
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            """height must be an integer"""
            raise TypeError("height must be an integer")
        if value < 0:
            """height must be greater than 0"""
            raise ValueError("height must be >= 0")
        self.__height = value


my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
