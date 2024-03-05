#!/usr/bin/python3
"""git commits"""

from sys import argv
from requests import get


if __name__ == '__main__':
    repo_name = argv[2]
    owner = argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo_name)
    res = get(url)

    for commit in res.json()[:10]:
        auther = commit['commit']
        print("{} {}".format(commit['sha'], commit['commit']['author']['name']))
