#!/usr/bin/python3
"""
'8-model_state_fetch_first' module, uses SQLAlchemy to list the first state object from a database
"""
if __name__ == '__main__':
    try:
        from model_state import Base, State
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        import sys

        # Create engine and session
        engine = create_engine(
            f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}")
        Session = sessionmaker(bind=engine)

        # Create session
        with Session() as session:
            # Query for the first State object
            state = session.query(State).first()

            # Print state information
            if state:
                print(f"{state.id}: {state.name}")
            else:
                print("Nothing")

    except Exception as e:
        print(f"Error: {e}")
