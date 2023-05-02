#!/usr/bin/python3
"""BAse geometry rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square """
    def __init__(self, size):
        """__init__"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
