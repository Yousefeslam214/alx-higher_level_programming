#!/usr/bin/python3
"""base"""


class BaseGeometry:
    """BaseGeometry empty class"""
    def area(self):
        """Method Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ instance method that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
