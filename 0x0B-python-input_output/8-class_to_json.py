#!/usr/bin/python3
""" 
My class module
"""


def class_to_json(obj):
    """retuns the dictionary description with simple data structure """

    structure = {}
    if hasattr(obj, "__dict__"):
        structure = obj.__dict__.copy()
    return structure
