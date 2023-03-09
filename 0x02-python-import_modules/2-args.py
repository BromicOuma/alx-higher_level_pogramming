#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    """
    print arguments stored in argument list

    """
    length = (len(argv))
    if length == 1:
        print("{:d} arguments.".format(length - 1))
    elif length == 2:
        print("{:d} argument:".format(length - 1))
        print("{:d}: {} ".format((length - 1), argv[1]))
    else:
        print("{:d} arguments:".format(length - 1))
        for i in range(length - 1):
            print("{:d}: {}".format((i + 1), argv[i + 1]))
