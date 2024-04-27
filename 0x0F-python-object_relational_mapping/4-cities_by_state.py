#!/usr/bin/python3

'''Script that lists all cities from the database 'hbtn_0e_0_usa'.'''

import MySQLdb
import sys


def list_cities(user, passwd, db):
    """List all cities from the database"""
    try:
        db_settings = {
            'host': 'localhost',
            'port': 3306,
            'user': user,
            'passwd': passwd,
            'db': db,
            'charset': 'utf8'
        }

        # Connect to the database
        with MySQLdb.connect(**db_settings) as db_conn:
            with db_conn.cursor() as cursor:
                # Execute the query
                query = "SELECT cities.id, cities.name, states.name AS state_name " \
                        "FROM cities JOIN states ON cities.state_id = states.id " \
                        "ORDER BY cities.id ASC"
                cursor.execute(query)
                rows = cursor.fetchall()

                # Print the results
                for row in rows:
                    print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    list_cities(username, password, database)
