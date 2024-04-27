#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''
from sys import argv
import MySQLdb


def list_states_by_name(user, passwd, db, argument):
    """List all states matching the provided name"""
    try:
        db_settings = {
            'host': 'localhost',
            'port': 3306,
            'user': user,
            'passwd': passwd,
            'db': db,
            'charset': "utf8"
        }

        # Connect to the database
        with MySQLdb.connect(**db_settings) as conn:
            with conn.cursor() as cur:
                # Execute the query
                query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
                cur.execute(query, (argument,))
                query_rows = cur.fetchall()

                # Print the results
                for row in query_rows:
                    print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    if len(argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <name>")
        exit(1)

    username, password, database, name = argv[1:]
    list_states_by_name(username, password, database, name)
