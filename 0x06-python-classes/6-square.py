#!/usr/bin/python3
'''
Definition of a class Square that
defines a square by: (based on 4-square.py)
'''


class Square:
    ''' A class dealing with a Square '''

    def __init__(self, size=0, position=(0, 0)):
        ''' initiation of a calss has args
        size (int): Private instance attribute
        position (axis): Private instance attribute
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''
        retrive the size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        set the value of the property
        '''
        # check if the size int or not
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    # Position property
    @property
    def position(self):
        '''
        retrive the position
        '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' set the Value of position '''
        if type(value) is tuple:
            _filter = filter(lambda x: type(x) is int and x >= 0, value)
            if len(list(_filter)) == 2:
                self.__position = value
                return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''
        returns the area of the Square
        '''
        return self.__size**2

    def my_print(self):
        '''
        prints in stdout the square with the character #
        '''

        if self.__size > 0:
            print("\n" * self.__position[1], end="")
            line = " " * self.__position[0] + "#" * self.__size + "\n"
            print(line * self.__size, end="")
        else:
            print()
