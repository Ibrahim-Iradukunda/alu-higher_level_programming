#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        bool: True if obj is an instance.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
