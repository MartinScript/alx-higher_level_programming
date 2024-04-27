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
            # Query all State objects and their associated City objects
            states = session.query(State).order_by(State.id).all()
            for state in states:
                print(f'{state.id}: {state.name}')
                for city in state.cities:
                    print(f'\t{city.id}: {city.name}')

    except Exception as e:
        print(f"Error: {e}")
