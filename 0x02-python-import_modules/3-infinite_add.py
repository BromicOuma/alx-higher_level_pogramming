#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    """
    infinite addition of cormant line arguments

    """
    sum = 0

    length = len(argv)
    for i in range(length):
        if i == 0:
            continue
        sum += int(argv[i])
    print("{:d}".format(sum))
