#!/usr/bin/python3
"""
'11-model_state_insert' module, uses SQLAlchemy to insert a new state object into the database
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
            # Create a new state object
            state = State(name="Louisiana")

            # Add the new state object to the session and commit changes
            session.add(state)
            session.commit()

            # Print the ID of the newly inserted state object
            print(state.id)

    except Exception as e:
        print(f"Error: {e}")
