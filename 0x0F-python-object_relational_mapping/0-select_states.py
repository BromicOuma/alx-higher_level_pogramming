#!/usr/bin/python3
"""module lists all the states from database"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    """main execution starts here printing all
        states from database passed as cmd line argument """

    my_db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                            passwd=argv[2], db=argv[3])

    my_cur = my_db.cursor()

    my_cur.execute('SELECT * FROM states')
    rows = my_cur.fetchall()
    for row in rows:
        print(row)
