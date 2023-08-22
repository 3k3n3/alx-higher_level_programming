#!/usr/bin/python3
"""Add State Louisana to hbtn_0e_6_usa."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    """Connect to db and excute query."""
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ),
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert into db
    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    # Print new id
    state = session.query(State).filter(
            State.name == "Louisiana").first()
    print(state.id)

    # close conection to db
    session.close()
