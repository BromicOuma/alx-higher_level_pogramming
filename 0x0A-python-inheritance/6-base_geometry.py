#!/usr/bin/python3
"""BaseGeometry raises an exception """


class BaseGeometry:
    """Base geometry class """
    def area(self):
        raise Exception('area() is not implemented')
