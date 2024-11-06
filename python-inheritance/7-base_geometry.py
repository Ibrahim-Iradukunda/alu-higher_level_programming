#!/usr/bin/python3
"""
Module 7-base_geometry
Contains a class BaseGeometry with an unimplemented area method 
and an integer validation method.
"""

class BaseGeometry:
    """BaseGeometry class for geometric operations"""

    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is an integer and greater than 0
        Args:
            name (str): name of the parameter
            value (int): value to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
