# pcost.py
#
# Exercise 1.27


total_cost = 0
f = open('Data/portfolio.csv', 'rt')
header = next(f)
for line in f:
    row = line.split(',')
    total_cost = total_cost + (int(row[1]) * float(row[2]))
f.close()

print('Total Cost', total_cost)



# Exercise 1.30 - 1.31

def portfolio_cost(filename):
	total_cost = 0
	f = open(filename, 'rt')
	header = next(f)
	for line in f:
		row = line.split(',')
		try:
			total_cost = total_cost + (int(row[1]) * float(row[2]))
		except ValueError:
			print("Something is missing", line)
		
	f.close()
	return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost using function:', cost)

# Exercise 1.32, 2.16
import csv
def portfolio_cost_csv_lib(filename):
	total_cost = 0
	f = open(filename)
	rows = csv.reader(f)
	headers = next(rows)
	#print(headers)
	for i,row in enumerate(rows):
		#record = {}
		record = dict(zip(headers, row))
		#print(record)
		try:
			total_cost = total_cost + (int(record['shares']) * float(record['price']))
		except ValueError:
			print("Something is missing in ", row, "with row number", i)

	f.close()
	return total_cost

cost = portfolio_cost_csv_lib('Data/portfolio.csv')
print('Total cost using csv module:', cost)


# Exercise 1.33, 2.15

import sys

def portfolio_cost_command_line(filename):
	total_cost = 0
	f = open(filename)
	rows = csv.reader(f)
	header = next(rows)
	for i,row in enumerate(rows):
		try:
			total_cost = total_cost + (int(row[1]) * float(row[2]))
		except ValueError:
			print("Something is missing in ", row, "with row number", i)

	f.close()
	return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost using command line:', cost)