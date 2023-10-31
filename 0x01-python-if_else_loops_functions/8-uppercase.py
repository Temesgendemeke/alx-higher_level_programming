#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
             ch = chr(ord(char) - 32)
        else:
            ch = char
        print("{:s}".format(ch), end="")
    print()
