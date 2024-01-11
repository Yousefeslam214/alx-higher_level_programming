#!/usr/bin/python3
""" function that creates an Object from"""
import json



def load_from_json_file(filename):
    """ function that creates an Object from"""
    with open(filename) as file:
        return json.load(file)
