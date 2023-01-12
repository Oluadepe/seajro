#!/usr/bin/python3
""" Defines the base model for all classes. """
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models


Base = declarative_base()


class GenModel():
    """
    defines all common attributes for all other classes
    attrs:
        id:          identity string
        created_at:  time created
        updated_at:  time updated
    """
    id = Column(String(60), nullable=False, unique=True, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated']:
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()

    def save(self):
        """ update the 'updated_at' time """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """ deletes current instance from storage """
        models.storage.delete(self)

    def __str__(self):
        """string representation of class """
        return "[{:s}] with identity number: ({:s})\n{}\n{}\n{}".format(
               self.__class__.__name__, self.id, '*' * 75, self.__dict__,
               '*' * 75)
