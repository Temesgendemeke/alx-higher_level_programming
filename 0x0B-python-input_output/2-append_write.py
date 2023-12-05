#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    >>> append_write("tests//my_first_file.txt", "This School is so cool!\n")
    24
    """
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
