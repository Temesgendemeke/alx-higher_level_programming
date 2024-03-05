#!/usr/bin/python3
"""_summary_"""


from sys import argv
from urllib.request import Request, urlopen

if __name__ == '__main__':
    with urlopen(argv[1]) as response:
        body = response.read()
        for head in response.getheaders():
            if head[0] == 'X-Request-Id':
                print(head[1])
