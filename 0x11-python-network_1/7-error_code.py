#!/usr/bin/python3
"""
Script that takes in URL, sends a request to URL
displays body of response
"""
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    status = r.status_code
    print(r.text) if status < 400 else print(
        "Error code: {}".format(r.status_code))
