#!/usr/bin/python3
"""New Engine DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os


classes = {'User': User, 'Place': Place, 'Review': Review,
           'State': State, 'City': City}


class DBStorage:
    """Class DBStorage for database in mysql"""
    __engine = None
    __session = None

    def __init__(self):
        """initialize class method"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == " test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects depending of the class name"""
        objects = {}
        for current_class in classes.values():
            if current_class is cls or cls is None:
                for elem in self.__session.query(current_class).all():
                    objects[elem.__class__.__name__+'.'+elem.id] = elem
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
        self.__session.close_all()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            for clas in self.__session.query(obj).all():
                self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(s)

    def close(self):
        """close() on the class Session"""
        self.__session.close()
