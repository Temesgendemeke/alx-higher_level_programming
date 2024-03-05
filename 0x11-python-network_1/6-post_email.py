#!/usr/bin/python3
"""_summary_"""


from requests import post
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = {"email": argv[2]}
    res = post(url, data=email)
    print(res.text)
