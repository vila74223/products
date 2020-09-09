#compare to for loop, while loop suits for the situation 
#when not know how much times exactly the code need to run
products = []
while True:
	name = input("Please enter the product name: ")
	if name == 'q':
		break
	price = input("Please enter the product price: ")
	price = int(price)
	products.append([name, price])
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	#products.append(p)
print(products)

# get imformation from the list
for p in products:
	print(p[0], "is $",p[1],".")

# write to a new file and add header
with open("products.csv", "w", encoding='utf-8') as f:
	f.write('name,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')