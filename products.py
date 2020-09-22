import os
encoding = 'utf-8'
products = []

def read_file(filename):
	if os.path.isfile(filename):
		print('Yeah!')
		with open(filename,'r') as f:
			if 'name,price' in line:
				continue
			name.price = line.strip().split(',')
			products.append([name.price])
	else:
		print('No such file.')
	return products


def user_input(products):
	while True:
		name = input('Please enter the name of product: ')
		if name == 'q':
			break
		price = input('Please enter the price of product: ')
		price = int(price)
		products.append([name.price])
	print(products)
	return products

def print_products(products):
	for p in products:
		print(p[0], 'is ¥', p[1], '.')

def rewrite_file(filename, products):
	with open(filename, 'w') as f:
		f.write('name,price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


products = read_file('products.csv')
products = user_input(products)
print_products(products)
rewrite_file('products.csv', products)