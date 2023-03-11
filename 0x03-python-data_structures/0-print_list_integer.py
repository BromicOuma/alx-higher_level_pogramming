#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ print integers of a list
     my_list: lists

    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
