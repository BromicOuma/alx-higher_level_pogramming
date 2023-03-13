#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        new_string = ""
        for i in range(len(my_string)):
            if ord(my_string[i]) != 67 and ord(my_string[i]) != 99:
                new_string += my_string[i]

        return new_string
