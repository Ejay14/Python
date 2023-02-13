#Author: Jabulani Mavodze
#Task L1T08
#Compulsory Task 1
#Date :29 January 2022

#This block of code requests for user input and declares the variables price,dist and Total_cost
price = float(input("Please enter the price of the package you would like to purchase.\n"))
dist = float(input("Please enter the total distance of the delivery in kilometres.\n"))
Total_cost = price

#This block of code presents options for a user to choose from by entering 1 OR 2.
print("Please select one option by entering 1 OR 2 :\n")
delivery_type = int(input("1.(Delivery via air) | 2.(Delivery via freight)\n"))
insurance = int(input ("1.(Full insurance) | 2.(Limited insurance)\n"))
gift = int(input("1.(Gift option) | 2.(NO gift)\n"))
delivery = int(input("1.(Priority Delivery) | 2.(Standard Delivery)\n"))

#This block of code uses control structures(IF-ELSE) , and then it alters the value of Total_cost.
if delivery_type == 1:
	Total_cost += dist*0.36
else:
	Total_cost += dist*0.25
	
if insurance == 1:
	Total_cost += 50.00
else:
	Total_cost += 25.00
	
if gift == 1:	
	Total_cost += 15.00
else:
	Total_cost += 0.00
	
if delivery == 1:
	Total_cost += 100.00
else:
	Total_cost += 20.00
	
print(f"The total cost of your package is: ${Total_cost}")					
 
