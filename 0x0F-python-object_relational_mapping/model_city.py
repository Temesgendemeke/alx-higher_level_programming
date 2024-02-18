#!/usr/bin/python3
"""Python file similar to model_state.py named model_city.py that contains the class definition of a City."""
from model_state import Base, State
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sys import argv
    
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"),  nullable=False)
        

        
    
