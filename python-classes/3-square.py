#!/usr/bin/python3
"""
Module 3-square
Defines a class Square with private instance attribute size and validation.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a private instance attribute size.
        Args:
            size (int): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: area of the square
        """
        return self.__size ** 2
