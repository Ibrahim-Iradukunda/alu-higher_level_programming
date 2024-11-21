#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status
using urllib and displays the body of the response.
"""

import urllib.request
import urllib.error

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode('utf-8')))
    except urllib.error.URLError as e:
        print("<urlopen error {}>".format(e.reason))
