#!/usr/bin/python3
""" State Module for HBNB project """
from AirBnB_clone2 import models
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    storageType = getenv('HBNB_TYPE_STORAGE')
    if storageType == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """getter attribute cities"""
            rlist = []
            dictCity = models.storage.all(City)
            for id, obj in dictCity.items():
                if id == obj.state_id:
                    rlist.append(obj)
            return rlist
        