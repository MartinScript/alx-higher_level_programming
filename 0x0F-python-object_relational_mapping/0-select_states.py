#!/usr/bin/python3
'''This script displays states by ID in ascending order'''

from sys import argv
import MySQLdb

if __name__ == '__main__':

    # declaring arguments passed.
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    # creating connection to the database.
    db_connection = MySQLdb.connect(host="localhost", port=3306, user=user,
                                    passwd=passwd, db=db, charset="utf8")

    # Making a cursor Object for query execution.
    cursor = db_connection.cursor()

    # Executing query.
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()

    # Printing DATABASE
    for row in query_rows:
        print(row)

    cursor.close()
    db_connection.close()
