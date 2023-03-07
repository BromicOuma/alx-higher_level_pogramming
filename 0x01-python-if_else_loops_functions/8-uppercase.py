#!/usr/bin/python3

def uppercase(str):

    new_strng = ""
    length = len(str)
    for i in range(length):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            new_strng = new_strng + chr(ord(str[i]) - 32)
            continue
        new_strng = new_strng + str[i]
    print(f"{new_strng}")
