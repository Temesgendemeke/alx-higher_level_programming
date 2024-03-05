#!/usr/bin/python3
"""_summary_"""


from sys import argv
from urllib.request import urlopen
from urllib import request, parse

if __name__ == '__main__':
    data = {"email": argv[2]}
    encode_data = parse.urlencode(data).encode("ascii")
    req = request.Request(argv[1], encode_data)
    with urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
