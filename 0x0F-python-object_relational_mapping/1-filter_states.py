#!/usr/bin/python3

'''Script that lists all states from the database 'hbtn_0e_0_usa'.'''

import MySQLdb
import sys


def connect_to_database(user, password, database):
    """Connect to MySQL database"""
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=user,
                             passwd=password, db=database)
        return db
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        sys.exit(1)


def list_states_starting_with_n(user, password, database):
    """List all states starting with 'N'"""
    db = connect_to_database(user, password, database)
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            if row[1].startswith('N'):
                print(row)
    except MySQLdb.Error as e:
        print(f"Error executing MySQL query: {e}")
    finally:
        cursor.close()
        db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    list_states_starting_with_n(username, password, database)
