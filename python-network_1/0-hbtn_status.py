#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status
using urllib and displays the body of the response.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))
