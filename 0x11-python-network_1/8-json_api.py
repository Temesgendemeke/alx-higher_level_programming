#!/usr/bin/python3
"""_summary_"""


from requests import get, post
from sys import argv

if __name__ == '__main__':
    q = argv[1]
    if len(argv) == 1 or not q.isalpha():
        print("No result")
        q = ""
    res = post("http://0.0.0.0:5000/search_user", data=q)
    
    print(res)
    
    
    