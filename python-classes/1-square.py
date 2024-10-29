#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with a private instance attribute size.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes the square with a private instance attribute size.
        Args:
            size: size of the square
        """
        self.__size = size
