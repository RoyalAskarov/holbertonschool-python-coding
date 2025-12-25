#!/usr/bin/python3
"""
This module defines a Square class.
The class is used to represent geometric squares with a private size attribute.
"""


class Square:
    """
        A class that defines a square.

        Attributes:
            __size (int): The length of a side of the square.
    """
    def __init__(self, size):
        self.__size = size
