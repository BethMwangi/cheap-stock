#!/usr/bin/env python
import os
import click
import  sys
import colorama 
from colorama import init, Fore, Back, Style



from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from models import Base, Stock
import docopt_config

engine = create_engine('sqlite:///./database.db')
Base.metadata.bind = engine

# associate with the custom Session class
DBSession = sessionmaker(bind=engine)
session = DBSession()




@click.group()
def cli():
    docopt_cmd()
    Stock()



def list_stock():
    """lists all the stock stored in table"""
    click.echo(click.style('TABLE LIST',  fg='green', bold=True , underline=True))
    stock = select([Stock])
    result = stock.execute()
    if result:
        for row in result:
            query = session.query(Stock).all()

            stock_list = [q for q in query]
    return stock_list


def query_currency(code):
    """Lists  the currency code a user inputs"""

    currency = session.query(Stock).filter(Stock.code == code).all()
    if currency:
        for curr in currency:
             return curr
    else:   
        return "Currecny does not exist"


            
   
