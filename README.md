# cheap-stock Application



> A  CLI python application that runs inside the terminal
> enabling the users to lists stock and query
> a given stock from the db list.

The user can:

 - View the list of currency with their respective code and country
 - Retrieve a currency code by given code


 The required commands for the application include;

1. `list_all ` - The user can be able to lists the currencies
2. `stock query_currency <code> `- The user can be able to query a given currency code



#Installation.

**To be able to get this project to your local machine**


```sh
$ git clone git@github.com:BethMwangi/cheap-stock.git
$ cd cheap-stock
$ . venv/bin/activate
$ pip3 install -r requirements.txt
$ pip3 install --editable .

```

"""
	Usage:
        stock list_all 
		stock query_currency <code> 
		
	Options:
		-h, --help Show this screen 
		--version Show version
"""