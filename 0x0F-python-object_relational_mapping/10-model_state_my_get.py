#!/usr/bin/python3
"""
'10-model_state_my_get' module, uses SQLAlchemy to query a state object from a database
"""
if __name__ == '__main__':
    try:
        from model_state import Base, State
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        import sys

        # Database connection string
        connection = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}"

        # Create engine and session
        engine = create_engine(connection)
        Session = sessionmaker(bind=engine)

        # Create session
        with Session() as session:
            # Query for the state object based on the provided state name
            state = session.query(State).filter(
                State.name == sys.argv[4]).first()

            # Print state information
            if state:
                print(state.id)
            else:
                print("Not found")

    except Exception as e:
        print(f"Error: {e}")
