import click
import sys
import time
from colorama import init
from tabulate import tabulate

def header():
	click.secho('$' * 70, fg='yellow')
	click.secho('=' * 70, fg='green')
	click.secho('STOCK CLI APP', blink=True, bold=True)
	click.secho('=' * 70, fg='green')
	click.secho('$' * 70, fg='yellow')




def start():
	time.sleep(2)
	click.secho(
        """
================LET'S GET STARTED============
GUIDE:
1.STOCK QUERY - query_currency <code> 
2.STOCK LIST - list_all 

Options:
		-h, --help Show this screen 
		--version Show version

==============================================
    """, bold=True, fg="yellow")




