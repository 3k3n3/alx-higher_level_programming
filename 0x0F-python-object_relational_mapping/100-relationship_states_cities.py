#!/usr/bin/python3
"""Add State & City: California & San Francisco to hbtn_0e_100_usa."""

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

    # Insert into db
    cali = State(name="California")
    san_fr = City(name="San Francisco")
    cali.cities.append(san_fr)

    session.add(cali)
    session.commit()

    # close conection to db
    session.close()
