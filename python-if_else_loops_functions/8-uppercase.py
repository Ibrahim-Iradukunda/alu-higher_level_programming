#!/usr/bin/env python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by adjusting ASCII value
            result += chr(ord(char) - 32)
        else:
            # Keep the character as is (for uppercase and non-alphabetic characters)
            result += char
    # Print the result followed by a new line
    print("{}".format(result))
# Example usage
uppercase("best")
uppercase("Best School 98 Battery street")
