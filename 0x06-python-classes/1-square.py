#!/usr/bin/python3
''' a class Square that defines a square by: (based on 0-square.py)'''


class Square:
    ''' class dealing with a square '''

    def __init__(self, size):
        ''' initiation of the class
        args:
        size (int): Private instance attribute
        '''
        self.__size = size
