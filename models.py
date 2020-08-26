import os
import sys
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Stock(Base):
    """Table that stores the stock info"""
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    country = Column(String(255), unique=False)
    currency = Column(String(255), unique=False)
    code = Column(String, unique=False)

    def __str__ (self):
    	return '{} - {} - {}'.format(self.country, self.currency, self.code)





engine = create_engine('sqlite:///./database.db')
Base.metadata.create_all(bind=engine)