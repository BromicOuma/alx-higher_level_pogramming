#!/usr/bin/python3
"""module appends to file"""


def append_write(filename="", text=""):
    """function to append to the end of a file """
    with open(filename, 'a', encoding='utf-8') as fp:
        return (fp.write(text))
