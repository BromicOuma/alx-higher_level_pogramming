#!/usr/bin/python3
"""A class Rectangle."""


class Rectangle:
    """A class that defines a rectangle.

    Attributes:
        __height (int): The height of the rectangle.
        __width (int): The width of the rectangle.

    Raises:
        TypeError: If the input parameter is not an integer.
        ValueError: If the input parameter is less than or equal to zero.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.__height = self.__valid_height(height)
        self.__width = self.__valid_width(width)

    @property
    def height(self):
        """Returns the height of the rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the input parameter is not an integer.
            ValueError: If the input parameter is less than or equal to zero.
        """

        self.__height = self.__valid_height(value)

    @property
    def width(self):
        """Returns the width of the rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the input parameter is not an integer.
            ValueError: If the input parameter is less than or equal to zero.
        """

        self.__width = self.__valid_width(value)

    def __valid_height(self, height):
        """Checks if the height parameter is valid.

        Args:
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the input parameter is not an integer.
            ValueError: If the input parameter is less than or equal to zero.

        Returns:
            int: The valid height of the rectangle.
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        return height

    def __valid_width(self, width):
        """Checks if the width parameter is valid.

        Args:
            width (int): The width of the rectangle.

        Raises:
            TypeError: If the input parameter is not an integer.
            ValueError: If the input parameter is less than or equal to zero.

        Returns:
            int: The valid width of the rectangle.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        return width

    @staticmethod
    def __check_type(value):
        """Checks if the input parameter is an integer.

        Args:
            value: The input value to check.

        Returns:
            bool: True if the value is an integer, False otherwise.
        """

        if isinstance(value, int):
            return True
        else:
            return False

    @staticmethod
    def __check_if_int(value):
        """Checks if the input parameter is greater than zero.

        Args:
            value: The input value to check.

        Returns:
            bool: True if the value is greater than zero, False otherwise.
        """

        if value > 0:
            return True
        else:
            return False
