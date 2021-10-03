#!/usr/bin/python3
'''creating a square'''


class square():
    '''class square'''
    __width = 0
    __height = 0

    def __init__(self, width, height):
        '''initializer'''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return value of size"""
        return self.__width

    @width.setter
    def size(self, number):
        """initialization method"""
        if type(number) is not int:
            raise TypeError("width must be an integer")
        if number < 0:
            raise ValueError("width must be >= 0")
        self.__width = number

    @property
    def height(self):
        """Return value of size"""
        return self.__height

    @height.setter
    def size(self, number):
        """initialization method"""
        if type(number) is not int:
            raise TypeError("height must be an integer")
        if number < 0:
            raise ValueError("height must be >= 0")
        self.__height = number

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__height

    def PermiterOfMySquare(self):
        '''square perimiter'''
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''string representation'''
        return "{}/{}".format(self.__width, self.__height)

if __name__ == "__main__":

    s = square(width=9, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
