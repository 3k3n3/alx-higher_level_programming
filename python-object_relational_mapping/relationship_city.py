#!/usr/bin/python3
"""Cities Class."""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """Cities Class."""
    __tablename__ = "cities"
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
        )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
