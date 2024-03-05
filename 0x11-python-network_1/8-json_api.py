#!/usr/bin/python3
"""_summary_"""


from requests import get, post
from sys import argv
import json

if __name__ == '__main__':
    letter = ""
    if len(argv) == 1:
        letter = ""
    letter = argv[1]
    payload = {"q": letter}
    res = post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
