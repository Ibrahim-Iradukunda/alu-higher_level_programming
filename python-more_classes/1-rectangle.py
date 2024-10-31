#!/usr/bin/python3
"""
Module 1-rectangle
Defines a class Rectangle.
"""


class Rectangle:
    """
    Represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle.
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        Args:
            value (int): width of the rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Args:
            value (int): height of the rectangle
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
