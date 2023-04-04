#!/usr/bin/python3
"""Class Rectangle that defines a rectangle """


class Rectangle:
    """__init__
    Clss init

    Atributes:

    Raises:
        TypeError: if not int
        ValueError : if less than 0
    """

    def __init__(self, width=0, height=0):
        """__innitializes the rectanles instance with width and height"""

        self.__height = self.__valid_height(height)
        self.__width = self.__valid_width(width)

    @property
    def height(self):
        """Return the height of the rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ Check the parameter height and if valid sets it """
        self.__height = self.__valid_height(value)

    @property
    def width(self):
        """Return the width of the rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ Check the parameter height and if valid sets it """
        self.__width = self.__valid_width(value)

    def __valid_height(self, height):
        """Check if the height is valid"""

        if self.__check_type(height) is False:
            raise TypeError("height must be a integer")

        if self.__check_if_int(height) is False:
            raise ValueError("height must be >= 0")

        self.__height = height
        return self.__height

    def __valid_width(self, width):
        """Check if the width is valid """

        if self.__check_type(width) is False:
            raise TypeError("width must be an integer")

        if self.__check_if_int(width) is False:
            raise ValueError("width must be >= 0")

        self.__width = width
        return self.__width

    @staticmethod
    def __check_type(value):
        """Check if type is int """

        if type(value) is int:
            return True

        else:
            return False

    @staticmethod
    def __check_if_int(value):
        """Check if the vlaue is an integer """

        if value > 0:
            return True

        else:
            return False
