#!/usr/bin/python3
"""DBstorage module
"""

import os
from models.base_model import BaseModel, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    '''DBStorage class'''

    __engine = None
    __session = None

    def __init__(self):
        '''To initialize an DBStorage instance'''

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(os.getenv("HBNB_MYSQL_USER"),
                   os.getenv("HBNB_MYSQL_PWD"),
                   os.getenv("HBNB_MYSQL_HOST"),
                   os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(bind=self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        '''Query on the current Db session all objects depending on
        the class name
        Return:
        Dictionary where
        key = <class-name>.<object-id>
        value = obj
        '''

        Dict = {}

        if cls:

            for intance in self.__session.query(cls):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

            return Dict

        else:

            for intance in self.__session.query(User):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

            for intance in self.__session.query(State):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

            for intance in session.query(City):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

            for intance in session.query(Amenity):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

            for intance in session.query(Place):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

            for intance in session.query(Review):
                key = '{}.{}'.format(type(instance).__name__, instance.id)
                Dict[key] = instance

        return Dict

    def new(self, obj):
        '''Add new obj to the current database session'''

        if obj:
            self.__session.add(obj)

    def save(self):
        '''commit all changes to the current database session'''

        self.__session.commit()

    def delete(self, obj=None):
        '''Delete current db session obj if not None'''

        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        '''Reload all the database'''

        Base.metadata.create_all(self.__engine)
