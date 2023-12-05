#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """
    function that reads a text file
    (UTF8) and prints it to stdout

    Args:
        filename (str, optional): filename to bre readed
    """
    with open(filename, encoding="utf-8") as files:
        print(files.read())
