#!/usr/bin/python3
""" """
from uuid import uuid4
from datetime import datetime


class GenModel():
    def __init__(self, *arg, **kwargs):
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
