#!/usr/bin/python3
"""Module with square class"""


class Square():
    """ square class
        class attributes:
            - width: width of a square
            - height: height of a square
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ constructor """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Returns area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Returns perimeter of the square"""
        return (self.width + self.height) * 2

    def __str__(self):
        """ str method to return str representation
            of an square instance
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
