#!/usr/bin/python3
"""
This script fetches http://0.0.0.0:5050/status
using urllib and displays the body of the response.
"""

import urllib.request

if __name__ == "__main__":
    url = 'http://0.0.0.0:5050/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))
