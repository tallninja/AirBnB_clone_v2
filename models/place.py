#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity

place_amenity = Table('place_amenity', Base.metadata, Column('place_id',
                      String(60), ForeignKey('places.id'), nullable=False),
                      Column('amenity_id', String(60),
                      ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
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

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref='place',
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False, cascade="all, delete",
                                 backref="places")

    else:

        @property
        def reviews(self):
            """
            Returns the list of Review instances with
            place_id equals to the current Place.id
            """
            from models import storage
            reviews_list = []
            for place in storage.all(Review).values():
                if place.id == self.place_id:
                    reviews_list.append(place)
            return reviews_list

        @property
        def amenities(self):
            """
            Function that returns the list of City
            instances with state_id
            """
            from models import storage
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id == self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def ameninities(self, arg):
            """ Function setter amenities """
            if arg.__class__.name__ == "Amenity":
                self.amenity_ids.append(arg)
