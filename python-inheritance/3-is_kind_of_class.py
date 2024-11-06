#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function that checks if an object is an instance.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        bool: True if obj is an instance of a_class or a subclass, else False.
    """
    return isinstance(obj, a_class)
