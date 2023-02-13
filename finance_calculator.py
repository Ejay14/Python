#Author: Jabulani Mavodze
#Task L1T11
#Compulsory Task 1(Capstone project)
#Date :30 January 2022

import math

#This block of code, present instrusctions to the user,
#it also declares and initialises the variable tmp to 1,
# ad last;y it takes user input from the user.
print("Choose either 'investment' or 'bond' from the menu below to proceed:")
print("investment      -to calculate the amount of interest you'll earn on interest")
print("bond	        -to calculate the amount you'll have to pay on a home loan")
tmp = 0
choice = input().lower() 


#This block of code uses a while loop to repetitively ask the user to enter the correct input, #if ever they enter an incorrect input.
#It then procceed to compute the simple interest, compound interest or bond repayment,
#using conditional statements and inputs from the user.
while(tmp == 0):
	if choice != "investment" and choice != "bond":
		print("Error, please choose either 'investment' or 'bond' from the menu above to proceed:")
		choice = input().lower() 
	else:
		tmp +=1
		
if choice == "investment":
	amount = int(input("Please enter the amount you want to deposit?:\n"))
	interest = float(input("please enter the interest (as a percentage):\n"))
	years = int(input("How many years do you plan to invest for:\n"))	
	interest_type = input("Do you want simple or compound interest:\n")
	
	if interest_type == "simple":
		gains = round((amount)*(1 + (interest/100)+years),2)
	else:
		gains = round((amount)*math.pow((1+(interest/100)),years),2)
		
	print(f"The amount you will get after {years} years, at the interest rate of {interest} is: R{gains}")
	
else:
	amount = int(input("Please enter the present value of the house:\n"))
	interest = float(input("please enter the interest (as a percentage):\n"))
	interest = interest/100
	months = int(input("Please enter the number of months you plan to repay the bond:\n"))	
	bond_payment = ((interest/100)*amount)/(1-math.pow(1+(interest/100),-months))
	print(f"The monthly bond repayment is: {bond_payment}")
	
				
	
	
