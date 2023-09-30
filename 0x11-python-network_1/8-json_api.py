#!/usr/bin/python3
"""Sends a search parameter to URL."""
import sys
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    a = [('q', query)]
    r = requests.post(url, data=a)
    try:
        json_content = r.json()
        if json_content:
            print('[{}] {}'.format(json_content['id'], json_content['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
