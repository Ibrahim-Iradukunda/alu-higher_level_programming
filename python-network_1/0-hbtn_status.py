#!/usr/bin/python3
"""
This script fetches http://0.0.0.0:5050/status
using urllib and displays the body of the response.
"""

import urllib.request

if __name__ == '__main__':
    url = 'http://0.0.0.0:5050/status'
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.URLError as e:
        print(e)
