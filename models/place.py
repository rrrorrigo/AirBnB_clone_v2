#!/usr/bin/python3
""" Place Module for HBNB project """
from AirBnB_clone2.models import amenity
from AirBnB_clone2.models.amenity import Amenity
from sqlalchemy.orm.relationships import foreign
from models.review import Review
import models
from sqlalchemy.orm import column_property, relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from os import getenv
metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                              Column('place_id', String(60), ForeignKey('places.id'),
                              primary_key=True, nullable=False),
                              Column('amenity_id', String(60), ForeignKey('amenities.id'),
                              primary_key=True, nullable=False)
                            )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    storageType = getenv('HBNB_TYPE_STORAGE')
    if storageType == 'db':
        reviews = relationship("Review", cascade="all, delete", backref="place")
        amenities = relationship("Amenity", cascade="all, delete", secondary='place_amenity', viewonly=False)
    else:
        @property
        def reviews(self):
            """getter method cities"""
            rlist = []
            dictReview = models.storage.all(Review)
            for id, obj in dictReview.items():
                if id == obj.state_id:
                    rlist.append(obj)
            return rlist

        @property
        def amenities(self):
            """getter method amenities"""
            rlist = []
            dictAmenities = models.storage.all(Amenity)
            for id, obj in dictAmenities.items():
                if id == obj.state_id:
                    rlist.append(obj)
            return rlist

        @amenities.setter
        def amenities(self, obj):
            """setter method amenities"""
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)