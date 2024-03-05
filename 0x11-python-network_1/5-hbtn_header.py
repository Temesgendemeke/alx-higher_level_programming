#!/usr/bin/python3
"""_summary_"""


from requests import get, post
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    res = get(url)
    try:
        print(res.headers['X-Request-Id'])
    except KeyError:
        pass
