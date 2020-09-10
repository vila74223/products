########read file############
products = []
with open("products.csv", 'r', encoding='utf-8') as f:
	for line in f:
		# s = line.strip().split(',')
		# name = s[0]
		# price = s[1]
		# print(s)
		# s is a list after split
		# ['name', 'price']
		# ['banana', '100']
		# ['apple', '200']
		# ['straberry', '800']
		# ['komanatsu', '130'] 
		# as it has already been split by comma, there are actually two blocks
		name, price = line.strip().split(',')
		products.append([name, price])
		# name, price is a list same as s
print(products)

########write file/add contents############
#compare to for loop, while loop suits for the situation 
#when not know how much times exactly the code need to run
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
	if 'name, price' in p:
		continue
	print(p[0], "is $",p[1],".")

########rewrite the file############
with open("products.csv", "w", encoding='utf-8') as f:
	f.write('name,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')