#!/usr/bin/python3
"""List all cities in hbtn_0e_101_usa."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
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

    # Get all cities
    states = session.query(State).join(City).order_by(City.id).all()
    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))

    # close conection to db
    session.close()
