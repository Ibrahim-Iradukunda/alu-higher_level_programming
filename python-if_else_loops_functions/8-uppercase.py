#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
# Testing the function with various cases
uppercase("holberton")
uppercase("Holberton School")
uppercase("Holberton School, 98 battery street")
uppercase("")
uppercase("98")
uppercase("z")
