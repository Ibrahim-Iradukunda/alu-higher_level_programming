#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line."""
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()  # Print a newline after the string
