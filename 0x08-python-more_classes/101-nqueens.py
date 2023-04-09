#!/usr/bin/python3
"""class solve n-queen """


class nqueen:
    """__init__
    innitialzes the class nqueen with value n

    Args:
        n (int) - size of the board i.e n by n and number of queens

    Return:
        the matix of the valid cell
    """

    def __init__(self, n):
        """__init__ class """
        if type(n) is not int:
            print("N must be a number")
            sys.exit(1)

        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        self.n = n


    def backtrack(self,):
        """class to backtrack """
        pass


    def isvalid(self, col, row):
        """isvalid checks isnthe current cell.is valid cell """
        col = ()
        post_diag = ()
        neg_diag = ()

        if c in col or (r - c) in post_diag or (r + c) in neg_diag:
            return False

        else:
            c4

        pass

