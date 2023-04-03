#!/usr/bin/python3
'''
Definition of a class Square that
defines a square by: (based on 4-square.py)
'''


class Square:
    ''' A class dealing with a Square '''

    def __init__(self, size=0):
        ''' initiation of a calss has args
        size (int): Private instance attribute
        '''
        self.__size = size

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

    def area(self):
        '''
        returns the area of the Square
        '''
        return self.__size**2

    def my_print(self):
        '''
        prints in stdout the square with the character #
        '''

        if not self.__size:
            print("")

        for i in range(self.__size):
            print('#'*self.__size)
