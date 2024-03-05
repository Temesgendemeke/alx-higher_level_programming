#!/usr/bin/python3
"""_summary_"""
from sys import argv
from urllib.request import Request, urlopen

with urlopen("https://www.google.") as response:
    body = response.read()
    body_code = body.decode('utf-8')
    print(body_code)
    
    