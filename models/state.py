#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from tokenize import String
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from models.city import City
from sqlalchemy.orm import backref
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state', cascade='all, delete')

    else:
        name = ""
    if models.storage != 'db':
        @property
        def cities(self):
            """ Returns the list of City
            """
            cities = []
            for c in models.storage.all(City).values():
                if c.state_id == self.id:
                    cities.append(c)
            return cities
