#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elements in matrix:
            i = 1
            length = len(elements)

            for idx in elements:
                if i == length:
                    print('{:d}'.format(idx), end='')
                else:
                    print('{:d}'.format(idx), end=' ')
                i += 1

            print()
