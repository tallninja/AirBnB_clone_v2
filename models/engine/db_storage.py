#!/usr/bin/python3
"""New engine DBStorage"""
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """Private class attributes:"""
    __engine = None
    __session = None
    classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        """ Public instance methods:
        """
        parameters = {
            "host": os.getenv("HBNB_MYSQL_HOST"),
            "port": 3306,
            "user": os.getenv("HBNB_MYSQL_USER"),
            "pass": os.getenv("HBNB_MYSQL_PWD"),
            "db": os.getenv("HBNB_MYSQL_DB")
            }
        self.__engine = create_engine(
            'mysql+mysqldb://{user}:{pass}@{host}:{port}/{db}'.format(
                **parameters), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """return a dictionary with all objets of a class or all classes"""
        mydict = {}
        if cls is None:
            for myclass in self.classes:
                result = self.__session.query(myclass).all()
                for obj in result:
                    mydict["{}.{}".format(obj.__class__, obj.id)] = obj
        else:
            result = self.__session.query(cls).all()
            for obj in result:
                mydict["{}.{}".format(obj.__class__, obj.id)] = obj
        return mydict

    def new(self, obj):
        """ add the object to the current database session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """ close method call remove()"""
        self.__session.close()
