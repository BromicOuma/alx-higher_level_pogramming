#!/usr/bin/python3
"""function that serializes the string """
import json


def to_json_string(my_obj):
    """to json string """
    return (json.dumps(my_obj))
