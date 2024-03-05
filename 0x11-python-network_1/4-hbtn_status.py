#!/usr/bin/python3
"""_summary_"""


from requests import get, post

if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    res = get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
