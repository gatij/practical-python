# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
def read_portfolio_as_list(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0],int(row[1]),float(row[2]))
            portfolio.append(holding)
    
    return portfolio 


# Exercise 2.5

def read_portfolio_as_dict(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
     
        for row in rows:
        	holding = {}
        	holding['name'] = row[0]
        	holding['shares'] = int(row[1])
        	holding['price'] = float(row[2])
        	portfolio.append(holding)
            
    
    return portfolio


# Exercise 2.6

def read_prices(filename):
	prices = {}
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		for row in rows:
			try:
				prices[row[0]] = row[1]
			except IndexError:
				print("Bad data in this row")
	return prices

holdings_list = read_portfolio_as_list('Data/portfolio.csv')
prices_dict = read_prices('Data/prices.csv')
pprint(holdings_list)
pprint(prices_dict)

P_L = 0
holding_P_L = 0
for holding in holdings_list:
	holding_P_L = ((float(prices_dict[holding[0]]) - holding[2]) * holding[1])
	print(holding[0], 'curr_price:', float(prices_dict[holding[0]]), 'Buy_price:', holding[2], holding_P_L)
	P_L += holding_P_L

print("NetP/L:", P_L)

	

    
    