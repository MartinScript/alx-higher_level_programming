#!/usr/bin/python3
"""This script displays states by ID in ascending order"""

import sys
import MySQLdb


def connect_to_database(user, passwd, db):
    """Connect to the MySQL database"""
    try:
        db_connection = MySQLdb.connect(host="localhost", port=3306, user=user,
                                        passwd=passwd, db=db, charset="utf8")
        return db_connection
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        sys.exit(1)


def display_states_by_id(user, passwd, db):
    """Display states by ID in ascending order"""
    db_connection = connect_to_database(user, passwd, db)
    cursor = db_connection.cursor()

    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cursor.fetchall()

        for row in query_rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error executing MySQL query: {e}")
    finally:
        cursor.close()
        db_connection.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    display_states_by_id(username, password, database)
