#!/usr/bin/python3
"""
Module 9-student
Defines a class Student with public instance attributes and a method.
"""


class Student:
    """
    A class to represent a student.
    
    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student with first_name, last_name, and age.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        Returns:
            dict: The dictionary representation of the student.
        """
        return self.__dict__
