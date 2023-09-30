#!/usr/bin/python3
"""
script that takes in URL, sends request to URL and displays
value of variable X-Request-Id in response header
"""

import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
