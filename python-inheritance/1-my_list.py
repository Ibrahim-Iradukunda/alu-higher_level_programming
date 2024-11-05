#!/usr/bin/python3

class MyList(list):
    """MyList that inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)  # Create a sorted version of the list
        print(sorted_list)          # Print the sorted list
