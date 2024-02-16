#!/user/bin/python3
"""_summary_"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, VARCHAR

Base = declarative_base()


class State(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'states'
    id = Column("id", Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True,)
    name = Column("name", VARCHAR(128), nullable=False)
