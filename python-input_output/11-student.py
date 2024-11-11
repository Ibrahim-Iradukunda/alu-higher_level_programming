#!/usr/bin/python3
"""
Module 11-student
Defines a class Student with public instance attributes.
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Args:
            attrs (list): A list of attribute names to retrieve.
        Returns:
            dict: The dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.
        Args:
            json (dict): The dictionary to update the instance attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
