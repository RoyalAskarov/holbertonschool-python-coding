#!/usr/bin/python3
"""
This module defines a Square class.
It uses properties for size validation and calculates the area.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The length of a side of the square.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2