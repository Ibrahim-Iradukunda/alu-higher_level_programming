#!/usr/bin/python3
"""
Module 8-rectangle
Defines a class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):



    """
    A class to represent a rectangle, inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
