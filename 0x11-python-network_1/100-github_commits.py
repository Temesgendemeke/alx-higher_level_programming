#!/usr/bin/python3
"""git commits"""

from sys import argv
from requests import get


if __name__ == '__main__':
    repo_name = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    res = get(url)

    commit = res.json()

    try:
        for i in range(10):
            print("{}: {}".format(commit[i]['sha'], 
                commit[i]['commit']['author']['name']))
    except IndexError:
        pass
