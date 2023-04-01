#!/usr/bin/python3

"""class square that define square """


class Square:
    """__init__

    The square initializatiom parameter

    Attributes:
        size (:obj: `int`, optional): The size of square

    Raises:
        TypeError: size is not int
        ValueError: value is less than 0


    """

    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be int")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """method returns the area of the square given size """

        return (self.__size * self.__size)
