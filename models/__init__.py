#!/usr/bin/python3
"""
initialize models package
"""
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
