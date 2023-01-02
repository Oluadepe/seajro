#!/usr/bin/python3
""" """
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.gen_model import GenModel, Base
from models.favourite import Favourite
from models.user import User
from models.feedback import Feedback
from os import getenv


classes = {'Favourite': Favourite, 'Feedback': Feedback, 'User': User}


class DBStorage:
    """ """
    __engine = None
    __session = None

    def __init__(self):
        """ instantiates DBStorage """
        SEAJRO_MYSQL_USER = getenv('SEAJRO_MYSQL_USER')
        SEAJRO_MYSQL_PWD = getenv('SEAJRO_MYSQL_PWD')
        SEAJRO_MYSQL_HOST = getenv('SEAJRO_MYSQL_HOST')
        SEAJRO_MYSQL_DB = getenv('SEAJRO_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(SEAJRO_MYSQL_USER,
                                             SEAJRO_MYSQL_PWD,
                                             SEAJRO_MYSQL_HOST,
                                             SEAJRO_MYSQL_DB),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """ make query on current database session """
        dictionary = {}
        if cls is None:
            for clss in classes.values():
                objects = self.__session.query(clss).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dictionary[key] = obj
        else:
            if type(cls) is str:
                cls = eval(cls)
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = obj.__class__.__name__ + '.' + obj.id
                dictionary[key] = obj

        return dictionary

    def new(self, obj):
        """ Add object to the current database session. """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session. """
        self.__session.commit()

    def delete(self, obj=None):
        """ """
        if obj is not None:
            self.__session.delete(obj)

    def get(self, cls, id):
        """ return cls object with the given ID. """
        if cls not in classes.values():
            return None
        else:
            all_classes = models.storage.all(cls)
            for obj in all_classes.values():
                if obj.id == id:
                    return obj

    def count(self, cls=None):
        """
        Counts objects in storage
        """
        if cls is None:
            for clss in classes.values():
                count = 0
                count += len(models.storage.all(clss).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def reload(self):
        """ create session and reloads data from database """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session

    def retrieve(self, user_cls, email):
        """ get user object by email """
        if type(user_cls) is str:
            user_cls = eval(User)
        dic = {}
        obj = self.__session.query(user).filter_by(email=email).first()
        key = obj.__class__.__name__ + '.' + obj.id
        dic[key] = obj
        return dic

    def close(self):
        """ close the session """
        self.__session.remove()
