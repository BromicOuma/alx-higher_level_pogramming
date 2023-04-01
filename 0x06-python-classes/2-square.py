#!/usr/bin/python3

"""A class square that defines a square """


class Square:
    """__init__

    the _init_ method initializes the square of size size

    Attributes:
        size (:obj:`int`, optional): The size of the square.

    Raises:
        TypeError: if size type is not int
        ValueError: if value ofnsize is less than 0

    """
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
