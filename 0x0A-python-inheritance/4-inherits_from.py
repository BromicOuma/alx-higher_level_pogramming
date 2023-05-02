#!/usr/bin/python3
"""checks where the class inherits from :"""


def inherits_from(obj, a_class):
    """inherits_from checks if the object inherits
    obj:
    a_class:

    returns:True or Fals
    """

    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
