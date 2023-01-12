#!/usr/bin/python3
""" This is the feedback class. """
from models.gen_model import GenModel, Base
from sqlalchemy import String, Column, ForeignKey


class Feedback(GenModel, Base):
    """ storage for user feedback """
    __tablename__ = 'feedbacks'
    user_email = Column(String(60),
                        ForeignKey('users.email', onupdate="CASCADE",
                                   ondelete="CASCADE"), nullable=False)
    city = Column(String(60), nullable=False)
    state = Column(String(60), nullable=False)
    country = Column(String(60), nullable=False)
    message = Column(String(2040), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Feedback"""
        super().__init__(*args, **kwargs)
