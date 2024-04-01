#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """Representation of a user """
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if kwargs.get('password'):
            self.password = kwargs['password']

    @property
    def password(self):
        """Password getter"""
        return self.__password

    @password.setter
    def password(self, value):
        """Password setter"""
        if value:
            self.__password = hashlib.md5(value.encode()).hexdigest()

    def to_dict(self):
        """Return a dictionary representation of the User instance"""
        if models.storage_t == 'db':
            # Include password in dictionary if storage type is 'db'
            return super().to_dict(include_password=True)
        else:
            return super().to_dict()
