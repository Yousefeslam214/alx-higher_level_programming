#!/usr/bin/python3
""" prints the list, but sorted"""


class MyList(list):
    """class"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
