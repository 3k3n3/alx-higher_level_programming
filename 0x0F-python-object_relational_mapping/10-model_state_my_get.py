#!/usr/bin/python3
"""Print state id of state passed as argument from hbtn_0e_6_usa."""

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

    # Retrieve form db

    states = session.query(State).filter(
            State.name == """{}""".format(sys.argv[4])
            ).first()
    # format and print output
    if states:
        print("{}".format(states.id))
    else:
        print("Not found")

    # close conection to db
    session.close()
