#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            size = int(size)
        except TypeError as exp:
            raise type(exp)("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
