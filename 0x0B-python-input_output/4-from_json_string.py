#!/usr/bin/python3
"""from json to string """
import json


def from_json_string(my_str):
    """function to convert json string to python
       object"""
    return (json.loads(my_str))
