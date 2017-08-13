#!/usr/bin/python3
"""
Contains class definition of State and an instance
Base = declarative_base():
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           unique=True, autoincrement=True,
                           primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    state_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy
                                 .ForeignKey('states.id'), nullable=False)
