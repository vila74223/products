#compare to for loop, while loop suits for the situation 
#when not know how much times exactly the code need to run
products = []
while True:
	name = input("Please enter the product name: ")
	if name == 'q':
		break
	price = input("Please enter the product price: ")
	products.append([name, price])
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	#products.append(p)
print(products)