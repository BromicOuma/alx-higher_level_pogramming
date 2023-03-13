#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = check_tuple(tuple_a)
    tup_b = check_tuple(tuple_b)

    return((tup_a[0] + tup_b[0]), (tup_a[1] + tup_b[1]))


def check_tuple(tuple=()):
    length = len(tuple)
    if length == 1:
        tuple = (tuple[0], 0)
    elif length >= 2:
        tuple = (tuple[0], tuple[1])
    elif length == 0:
        tuple = (0, 0)

    return tuple
