#!/usr/bin/python3
'''
Definition of a class Square that
defines a square by: (based on 1-square.py)
'''


class Square:
    ''' A class dealing with a Suare '''

    def __init__(self, size=0):
        ''' initiation of a calss has args
        size (int): Private instance attribute
        '''

        # check if the size int or not
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        # set the attribute
        self.__size = size
