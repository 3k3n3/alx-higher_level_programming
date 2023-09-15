#!/usr/bin/python3
"""Lists all states from hbtn_0e_6_usa."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    cities = session.query(City, State).join(State).order_by(City.id).all()
    # format and print output
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # close connection to db
    session.close()
