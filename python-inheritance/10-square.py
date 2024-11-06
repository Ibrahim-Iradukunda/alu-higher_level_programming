#!/usr/bin/python3
"""
Module 10-square
Defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class to represent a square, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the square with size.
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
