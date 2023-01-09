#!/usr/bin/python3
""" Module contains the representation of user's favourite. """
from models.gen_model import GenModel, Base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Favourite(GenModel, Base):
    """ defines favourite attribute """
    __tablename__ = 'favourites'
    country = Column(String(60), nullable=False)
    state = Column(String(60), nullable=False)
    city = Column(String(60), nullable=False)
    user_email = Column(String(60), ForeignKey('users.email'), nullable=False)

    def __init__(self, *arg, **kwargs):
        """initializes Favourite"""
        super().__init__(*args, **kwargs)
