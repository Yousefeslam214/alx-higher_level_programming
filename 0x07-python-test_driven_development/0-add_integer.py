#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, int):
        if isinstance(a, float):
            int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            int(b)
        else:
            raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
