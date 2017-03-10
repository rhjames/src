from __future__ import print_function
import os.path
from collections import defaultdict
import string
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://www.revisor.mn.gov/laws/?year=2014&type=0&doctype=Chapter&id=294"
# Init the variables
# Use a defaultdict with an empty list because it eases the DataFrame creation
expense_lines = defaultdict(list)
funding_lines = defaultdict(list)
funding = False

result = requests.get(url)
c = result.content
soup = BeautifulSoup(c)

def convert_num(val):
	val = string.strip(val).replace(",","").replace("(","-").replace(")","")
	return float(val)


# After looking at the data, we can see that the summary has a div id we can use
summary = soup.find("div", {"class":"bill_section","id": "laws.1.1.0"})

# Get all the tables in the summary
tables = summary.find_all('table')

# The first table is not useful header info
# The second table contains all the we need (the list is 0 indexed)
data_table = tables[1]

for row in data_table.find_all("tr"):
	cells = row.find_all("td")
	if len(cells) == 3:
		line = (string.strip(cells[0].text), convert_num(cells[2].text))
		if line[0] == "TOTAL":
			funding = True
            # We don't want to capture the total because we can calc it
        	continue
		if funding:
			funding_lines[line[0]].append(line[1])
        else:
        	expense_lines[line[0]].append(line[1])






