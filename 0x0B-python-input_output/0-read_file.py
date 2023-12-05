#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """
    >>> read_file("./test/my_file_0.txt")
    We offer a truly innovative approach to education:
    focus on building reliable applications and scalable systems,
    take on real-world challenges, collaborate with your peers.

    A school every software engineer would have dreamt of!
    """
    with open(filename, encoding="utf-8") as files:
        print(files.read())
