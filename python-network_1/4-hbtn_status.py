#!/usr/bin/python3
"""
This script fetches the status from the provided URL
using the requests package and displays the body of the response.
"""

import requests

def fetch_status(url):
    try:
        r = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
    except requests.RequestException as e:
        print(f"<Request error: {e}>")

if __name__ == "__main__":
    urls = ["https://alu-intranet.hbtn.io/status", "http://0.0.0.0:5050/status"]
    for url in urls:
        print(f"Fetching from {url}")
        fetch_status(url)
        print()

