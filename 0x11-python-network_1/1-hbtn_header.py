#!/usr/bin/python3
"""Takes URL and sends request and displays value of X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
