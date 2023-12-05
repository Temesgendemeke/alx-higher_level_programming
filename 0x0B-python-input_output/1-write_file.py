#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    >>> write_file("tests//my_first_file.txt", "This School is so cool!\n")
    24
    """
    with open(filename, "w", encoding="utf-8") as txtfile:
        return txtfile.write(text)
