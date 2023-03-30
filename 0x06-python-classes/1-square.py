#!/usr/bin/python3

"""Class defining a square """


class Square:
    """Square that initializes with
    the size  of a square"""

    def __init__(self, size):
        """__init__

        Innitializes the square with side variable"

        Attributes:
            size(int): side of the square

        """
        self.__size = size
