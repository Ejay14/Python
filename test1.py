

class Shoe:

	data = []
	
	def __init__(self,country,code,product,cost,quantity):
		self.country = country
		self.code = code
		self.product = product
		self.cost = cost
		self.quantity = quantity
	
	def read_data(self):
		try:
			with open("inve.txt", 'r') as f:
 				self.data = f.readlines()
		except:
 			print("Failed")
 
 
class shoe(Shoe):
	def __init__(self,country,code,product,cost,quantity,value): 
		super().__init__(country,code,product,cost,quantity)
		self.value = value
  	
shoe = Shoe("sa","12","nike","14","5")
shoe.read_data()
lists = []	
for i in range(25):
	content = (shoe.data[i]).split(",")
	print(content)
	country = content[0]
	code = content[1]
	product = content[2]
	cost = content[3]
	quantity = content[4]
	new_Shoe = Shoe(country,code,product,cost,quantity)
	lists.append(new_Shoe)


def dup(sL):
	matrix = []
	
	for i in range(25):
		nl = []
		st1 = lists[i].country 
		nl.append(st1)
		
		st2 = lists[i].code
		nl.append(st2)
		
		st3 = lists[i].product
		nl.append(st3)
		
		st4 = lists[i].cost
		nl.append(st4)
		
		st5 = lists[i].quantity
		nl.append(st5)
		matrix.append(nl)
	return matrix
	
	
def search(product):
	for i in lists:
		if i.product == product:
			print("Search results:")
			print(f"Country: {i.country}")
			print(f"Code: {i.code}")
			print(f"Product: {i.product}")
			print(f"Cost: R{i.cost}")
			print(f"Quantity: {i.quantity}")
search("Jordan 1")

def restock():
	tmp = int(lists[1].quantity)
	product = lists[1].product
	for i in range(1,25):
		if int(lists[i].quantity) < tmp:
			tmp = int(lists[i].quantity)
			product = lists[i].product
	print(f"The product with the lowest stock is the {product}, with {tmp} units in stock restock it")
			
			
restock()			
			
def Sale():
	tmp = int(lists[1].quantity)
	product = lists[1].product
	for i in range(1,25):
		if int(lists[i].quantity) > tmp:
			tmp = int(lists[i].quantity)
			product = lists[i].product
	print(f"The product with the highest stock is the {product}, with {tmp} units mark it up for sale")		
			
			
Sale()		

def value_per_item():
	value = ["Value"]
	count = 0
	for i in range(1,25):
			t  = int(lists[i].quantity)*int(lists[i].cost)
			value.append(str(t))
	
	with open("inve.txt", 'r') as f:
		lines = f.read().splitlines()
	with open("inve.txt",'w') as f:
		for line in lines:
			print(line +","+ value[count], file=f)
			if count < 25:
				count = count + 1
	
	
value_per_item()	
	
'''print(tabulate(dup(lists),headers='firstrow',tablefmt='github',showindex='always'))'''
	
