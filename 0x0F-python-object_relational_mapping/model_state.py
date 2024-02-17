#!/user/bin/python3
"""python file that contains the class definition of a State and an instance"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer,  String

Base = declarative_base()


class State(Base):
    """
    Attributes:
        id = ID state
        name: Name of state
    """
    __tablename__ = "states"
    id = Column( Integer, nullable=False, 
                primary_key=True, autoincrement=True,)
    name = Column(String(128), nullable=False)
