#!/usr/bin/python3
""" Module contains user class for the representation of user.
and user schedule events"""
from models.gen_model import GenModel, Base
from sqlalchemy import Integer, Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from hashlib import md5


class User(GenModel, Base):
    """ defines a user attributev"""
    __tablename__ = 'users'
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False, unique=True, primary_key=True)
    state = Column(String(60))
    city = Column(String(60))
    country = Column(String(60))
    # favourite_count = Column(Integer, default=0)
    # feedback_count = Column(Integer, default=0)
    events = relationship('Event', cascade="all, delete, save-update,\
                          delete-orphan", backref='User')
    favourites = relationship('Favourite', cascade="all, delete, save-update,\
                          delete-orphan", backref='User')
    feedbacks = relationship('Feedback', cascade="all, delete, save-update,\
                          delete-orphan", backref='User')

    def __init__(self, *arg, **kwargs):
        """initializes User"""
        super().__init__(*arg, **kwargs)

    def __setattr__(self, passwd, value):
        """ sets password with md5 encryption"""
        if passwd == 'password':
            value = md5(value.encode()).hexdigest()
        super().__setattr__(passwd, value)


class Event(GenModel, Base):
    """ storage for user schedules """
    __tablename__ = 'schedules'
    user_email = Column(String(60),
                        ForeignKey('users.email', ondelete="CASCADE",
                                   onupdate="CASCADE"), nullable=False)
    title = Column(String(200), nullable=False)
    date = Column(Date, nullable=False)
    country = Column(String(60), nullable=False)
    city = Column(String(60), nullable=False)
    state = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes event"""
        super().__init__(*args, **kwargs)
