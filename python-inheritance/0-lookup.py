#!/usr/bin/python3
"""
Module 0-lookup
Contains a single function..
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.
    Returns:
        List of attributes and methods of the object.
    """
    return dir(obj)
