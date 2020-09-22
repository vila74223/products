import os

def read_file(filename):
	products = []
	with open(filename,'r', encoding = 'utf-8') as f:
		for line in f:
			if 'name,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
			return products

def user_input(products):
	while True:
		name = input('Please enter the name of product: ')
		if name == 'q':
			break
		price = input('Please enter the price of product: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

def print_products(products):
	for p in products:
		print(p[0], 'is ¥', p[1], '.')

def rewrite_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('name,price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('Yeah!')
		products = read_file(filename)
	else:
		print('No such file.')
	
	products = user_input(products)
	print_products(products)
	rewrite_file('products.csv', products)

main()