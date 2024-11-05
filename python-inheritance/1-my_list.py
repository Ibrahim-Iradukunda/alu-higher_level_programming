#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    Inherits from list and adds a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
