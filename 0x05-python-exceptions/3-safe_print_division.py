#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        return (a / b)
    except ZeroDivisionError:
        return None
