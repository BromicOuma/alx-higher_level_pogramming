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

    def area(self):
        """Calculates the area of rectangle

        Args:
            None: Does not take any argumrnts

        Returns:
            int: The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the circle

        Args:
            None: Does not take any argument

        Returns:
            int: The perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * self.__width + 2 * self.__height

    def __draw_rectangle(self):
        """
        Draw the Rectangle with their size
        Returns:
            str: `Empty` If width or height is `0`,
            otherwise returns a string with the Rectangle.
        """

        rect_str = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += '#'

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    def __str__(self):
        """
        Returns a string with the representation of the Rectangle.
        """

        return self.__draw_rectangle()

    def __repr__(self):
        """
        Returns the representation of the Rectangle.
        """
        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'
