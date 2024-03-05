#!/usr/bin/python3
"""_summary_"""


from requests import get
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    res = get(url)
    if res.ok:
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))
