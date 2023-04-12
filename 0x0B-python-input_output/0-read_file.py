#!/usr/bin/python3
"""this module reads a file encoded in UTF8 """


def read_file(filename=""):
    """read file print to stdout """
    with open(filename, "r", encoding="utf-8") as fp:
        for lines in fp:
            print(lines, end='')
