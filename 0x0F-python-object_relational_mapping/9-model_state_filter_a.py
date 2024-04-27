#!/usr/bin/python3
'''Lists all State objects from the database hbtn_0e_6_usa where the state name contains the letter 'a'.'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    try:
        # Database connection string
        connection = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'

        # Create engine and bind session
        engine = create_engine(connection, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)

        # Create session
        with Session() as session:
            # Query for all State objects where the state name contains 'a'
            states = session.query(State).filter(
                State.name.contains('a')).order_by(State.id).all()

            # Print state information
            for state in states:
                print(f'{state.id}: {state.name}')

    except Exception as e:
        print(f"Error: {e}")
