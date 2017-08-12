#!/usr/bin/python3
"""
Contains class definition of State and an instance
Base = declarative_base():
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           unique=True, autoincrement=True,
                           primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
