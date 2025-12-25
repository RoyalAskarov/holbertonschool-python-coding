#!/usr/bin/python3
"""
This module defines a Square class.
It includes validation for size and a method to calculate the area.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The length of a side of the square.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
