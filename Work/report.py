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


# Exercise 2.23
# magic of comprehension 
def read_portfolio(filename):
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)

		select = ['name', 'shares', 'price']
		indices = [ headers.index(colname) for colname in select ]
		row = next(rows)
		portfolio = [ { col:row[index] for col,index in zip(select,indices) } for row in rows ]

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
				pass
		return prices

holdings_list = read_portfolio_as_list('Data/portfolio.csv')
prices_dict = read_prices('Data/prices.csv')
#pprint(holdings_list)
#pprint(prices_dict)



# Exercise 2.7
P_L = 0
holding_P_L = 0
for holding in holdings_list:
	holding_P_L = ((float(prices_dict[holding[0]]) - holding[2]) * holding[1])
	#print(holding[0], 'curr_price:', float(prices_dict[holding[0]]), 'Buy_price:', holding[2], holding_P_L)
	P_L += holding_P_L

print("NetP/L:", P_L, '\n')



# Exercise 2.9 - 2.12
headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f"{'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s} {'-'*10:>10s}")



def make_report(holdings_list,prices_dict):
	report = []
	for holding in holdings_list:
		report.append((holding[0], holding[1], float(prices_dict[holding[0]]), (float(prices_dict[holding[0]]) - holding[2])))
	return report

report = make_report(holdings_list,prices_dict)
for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$"+ str(round(price,2)):>10s} {change:>10.2f}')






    
    