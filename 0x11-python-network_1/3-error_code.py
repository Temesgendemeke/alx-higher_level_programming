#!/usr/bin/python3
"""_summary_"""


from sys import argv
from urllib.request import urlopen
from urllib import request
from urllib.error import HTTPError

if __name__ == '__main__':
    url = argv[1]
    try:
        with urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
