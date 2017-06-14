# Configuration
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///restaurant.db')

Base.metadata.create_all(engine)

__author__ = 'Karan'
