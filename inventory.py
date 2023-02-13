#=====importing libraries===========
from tabulate import tabulate

#=====Class Section===========
'''Here I will create a class called 'Shoe'.
	-The class will have one class variable, an array called 'data'.
	-The contructor of the class will initialise five variables namely:
		*country,code,product,cost and quantity.
	-The class has one fuction 'read_data()", that takes in zero parameters, 
	 the function is used to read in data from a txt file and populate the array.
'''
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
			with open("inventory.txt", 'r') as f:
 				self.data = f.readlines()
		except FileNotFoundError:
 			print("Failed:The file does not exist!")
 			
#=====Functions/Methods Section===========
'''Objects_first function:
	-This function takes in zero parameters.
	-This funtion is used to create Shoe objects and then put them in an array,
	 it uses the data from the array data in-order to create the objects.
	-This funtion returns a list of Shoe objects.
'''
def Objects_first():
	lists = []	
	for i in range(25):
		content = (shoe.data[i]).split(",")
		country = content[0]
		code = content[1]
		product = content[2]
		cost = content[3]
		quantity = content[4]
		new_Shoe = Shoe(country,code,product,cost,quantity)
		lists.append(new_Shoe)
	return lists
	
'''Search function:
	-This function takes in one parameter called 'product'.	
	-This function uses the list of objects created by the function 'Objects_first()',
	 to check if a certain product exists in the list, and if it does it prints the product's information,
	 i.e country, code etc.
	-This function does not have a return statement.
'''
def search(product):
	lists = Objects_first()
	once =  False
	for i in lists:
		if i.product == product:
			print("Search results:")
			print(f"Country: {i.country}")
			print(f"Code: {i.code}")
			print(f"Product: {i.product}")
			print(f"Cost: R{i.cost}")
			print(f"Quantity: {i.quantity}")
			once = True
			
	if once == False:
		print("Ooops product does not exist!")
'''restock function:
	-This function takes in zero parameters.
	-This function uses the list of objects created by the function 'Objects_first()',
	 to check for the product with the lowest stock.
	-This function does not have a return statement.
'''			
def restock():
	lists = Objects_first()
	tmp = int(lists[1].quantity)
	product = lists[1].product
	for i in range(1,25):
		if int(lists[i].quantity) < tmp:
			tmp = int(lists[i].quantity)
			product = lists[i].product
	print(f"The product with the lowest stock is the {product}, with {tmp} units in stock restock it.")	

'''sale function:
	-This function takes in zero parameters.
	-This function uses the list of objects created by the function 'Objects_first()',
	 to check for the product with the highest stock.
	-This function does not have a return statement.
'''	
def Sale():
	lists = Objects_first()
	tmp = int(lists[1].quantity)
	product = lists[1].product
	for i in range(1,25):
		if int(lists[i].quantity) > tmp:
			tmp = int(lists[i].quantity)
			product = lists[i].product
	print(f"The product with the highest stock is the {product}, with {tmp} units mark it up for sale.")	

'''value_per_item function:
	-This function takes in zero parameters.
	-This function uses the list of objects created by the function 'Objects_first()',
	 to calculate the total worth  of each  product using the formular 'value=cost*quantity and 
	 store the data in the array called 'value'.
	-This function also adds a new column to the 'inventory.txt' file and then it populates the column inthe filewith 
	 the data calculated.
	-This function returns the array 'value'.
'''	
def value_per_item():
	lists = Objects_first()
	value = ["Value"]
	count = 0
	for i in range(1,25):
			t  = int(lists[i].quantity)*int(lists[i].cost)
			value.append(str(t))
	
	with open("inventory.txt", 'r') as f:
		lines = f.read().splitlines()
	with open("inventory.txt",'w') as f:
		for line in lines:
			print(line +","+ value[count], file=f)
			if count < 25:
				count = count + 1	
	return value			

'''duplicate_data function:
	-This function takes in zero parameters.
	-This function uses the list of objects created by the function 'Objects_first()' and the array 'value' from the 'value_per_item()'
	 function,to format the data in such a way the (python's tabulate module) will process it easier without producing unnecessary 
	 white spaces between every character in the table due to encoding when reading the file .The format:
	 *[['South Africa','SKU44386','Air Max 90','2300','20','46000'],['Country','Code','Product','Cost','Quantity','Value']]
	-This function returns an array 'called'.
'''
def duplicate_data():
	lists = Objects_first()
	lists2 = value_per_item()
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
		
		st6 = lists2[i]
		nl.append(st6)
		matrix.append(nl)
	return matrix


#=====Logic Section===========
shoe = Shoe("null","null","null","null","null")
shoe.read_data()
user_choice = ""	
while user_choice != "quit":
	user_choice = (input("What would you like to do - search/restock/sale/view table/quit?\n")).lower()
	if user_choice == "restock":
		restock()
	elif user_choice == "sale":
		Sale()	
	elif user_choice == "search":
		product = input("Search product: ")
		search(product)
	elif user_choice == "view table":
		print(tabulate(duplicate_data(),headers='firstrow',tablefmt='github',showindex='always'))
	elif user_choice == "quit":
		print("Goodbye")
	else:
		print("Oops - incorrect input")
		
		
#NB:I have ran my code many times and i dont get the indentation error ,my code runs in my machine.
