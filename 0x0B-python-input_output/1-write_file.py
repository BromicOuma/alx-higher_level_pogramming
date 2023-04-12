#!/usr/bin/python3
"""module to write to a file, it creates one of it doesnt exist amd overwrites the contents """


def write_file(filename="", text=""):
    """write to a file from stdio """
    with open(filename, "w", encoding="utf-8") as fp:
        return (fp.write(text))#
