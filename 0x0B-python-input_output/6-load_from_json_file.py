#!/usr/bin/python3
"""module for loading from json """
from json import loads


def load_from_json_file(filename):
    """function to load from json file """
    with open(filename, encoding="utf-8") as fp:
        return loads(fp.read())
