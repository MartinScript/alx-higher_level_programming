#!/usr/bin/python3
'''Lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    try:
        # Database connection string
        connection = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"

        # Create engine and session
        engine = create_engine(connection, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        # Create session
        with Session() as session:
            # Create a new state object
            new_state = State(name="California")

            # Create a new city object
            new_city = City(name="San Francisco")

            # Append the city to the state's list of cities
            new_state.cities.append(new_city)

            # Add the new state and city objects to the session and commit changes
            session.add(new_state)
            session.commit()

    except Exception as e:
        print(f"Error: {e}")
