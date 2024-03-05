#!/usr/bin/python3
""" working with github api"""


from sys import argv
import requests

if __name__ == "__main__":
    auth = requests.auth.HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
