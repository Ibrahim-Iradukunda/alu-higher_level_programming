#!/usr/bin/python3
"""
Module 6-square
Defines a class Square.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.
        Args:
            size (int): size of the square
            position (tuple): position of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
            TypeError: if position is not a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        Args:
            value (tuple): position of the square
        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if (
not isinstance(value, tuple)
len(value) != 2 or
not all(isinstance(num, int) and num >= 0 for num in value)
):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #.
        If size is equal to 0, prints an empty line.
        Position should be used by using spaces.
        """
        if self.__size == 0:
            print()
        else:
            [print() for _ in range(self.__position[1])]
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
