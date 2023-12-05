#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """
    >>> write_file("tests//my_first_file.txt", "This School is so cool!\n")
    24
    """
    with open(filename, "r+", encoding="utf-8") as txtfile:
        write_data = txtfile.write(text)
        return write_data
