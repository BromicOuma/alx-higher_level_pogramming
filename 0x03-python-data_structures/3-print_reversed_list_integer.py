#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    if my_list:
        idx = length - 1
        while idx >= 0:
            print("{:d}".format(my_list[idx]))
            idx -= 1
