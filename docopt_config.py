"""
	Usage:
        stock list_all 
		stock query_currency <code> 
		
	Options:
		-h, --help Show this screen 
		--version Show version
"""

from docopt import docopt, DocoptExit
import cmd
import stock
import click
import ui



ui.header()
ui.start()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


stock_list = []
class Stock(cmd.Cmd):

    prompt = click.style(">>>stock", bg='green', fg='white', bold='True')

    @docopt_cmd
    def do_list_all(self, arg):
        """Usage: list_all"""
        import stock
        stock_list =  stock.list_stock()
        for stock in stock_list:
            print(stock)


    @docopt_cmd
    def do_query_currency(self, arg):
        """Usage: query_currency <code>"""
        code = arg["<code>"]
        self.stock_code =  stock.query_currency(code)
        print(self.stock_code)
      

if __name__ == '__main__':
    Stock().cmdloop()