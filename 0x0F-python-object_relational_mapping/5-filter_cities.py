#!/usr/bin/python3
"""
Script that lists all cities from the database 'hbtn_0e_0_usa' for a given state.
"""
import MySQLdb
import sys


def list_cities_by_state(user, passwd, db, state_name):
    """List all cities for a given state"""
    try:
        # Database connection settings
        db_settings = {
            'host': 'localhost',
            'port': 3306,
            'user': user,
            'passwd': passwd,
            'db': db,
        }

        # Connect to the database
        with MySQLdb.connect(**db_settings) as conn:
            with conn.cursor() as cur:
                # Execute the query
                query = "SELECT cities.name FROM cities " \
                        "JOIN states ON cities.state_id = states.id " \
                        "WHERE states.name = %s ORDER BY cities.id"
                cur.execute(query, (state_name,))
                rows = cur.fetchall()

                # Extract city names and join them into a string
                city_names = [row[0] for row in rows]
                city_str = ", ".join(city_names)
                print(city_str)

    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    list_cities_by_state(username, password, database, state_name)
