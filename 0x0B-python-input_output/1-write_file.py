#!/usr/bin/python3
"""main"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, encoding="utf-8") as file:
        file.write(text)
