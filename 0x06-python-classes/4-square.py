#!/usr/bin/python3

"""class square that defines a square"""


class Square:
    """__init__

    innitializes class with value size

    Attributes:
        size(:obj:`int`,optional): size of square

    Raises:
        TypeError: If value is not int
        VaueError: if value less than 0

   """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be int")

        if size < 0:
            raise ValueError("size mustbbe >= 0")

        return self.__size

    def area(self):
        """area given size """

        return (self.__size  ** 2)
