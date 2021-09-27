#!/usr/bin/python3

class square():
    
    width = 0
    height = 0

    
    def __init__(self, width=0, height=0):
        if type(width) is not int or type(height) is not int:
            raise TypeError("size must be an integer")
        if width != height:
            raise ValueError("width must be equal to height")

        self.width = width
    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
