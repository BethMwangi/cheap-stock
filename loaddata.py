#!/usr/bin/env python
import csv
import requests
import io
from urllib.request import urlopen


url = "https://focusmobile-interview-materials.s3.eu-west-3.amazonaws.com/Cheap.Stocks.Internationalization.Currencies.csv"

response = urlopen(url)
cr = csv.reader(io.TextIOWrapper(response, encoding = 'utf-8'), delimiter=',')

# for row in cr:
#     print(row)

# insert data to db