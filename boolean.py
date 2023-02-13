#Author: Jabulani Mavodze
#Task 6
#Compulsory Task 1
#Date :18 January 2022

#This block of code declares variables and then initializes them with the boolean value false.
have_length = False
up_case = False
low_case = False
have_num = False
count = 0

#This block of code requests user input,
#and then it alters the value of the variables delared above to the boolean value true if the condition is true.
#It also increases the counter by one if the condition is true.
print("Please enter (yes) OR (no) for the following questions\n")
length = input("Does your password have more than six characters?\n").lower()

if length == "yes":
	have_length = True
	count +=1
	
upper = input("Does your password have at least one upper case/capital letter?\n").lower()
if upper == "yes":
	up_case = True
	count +=1

lower = input("Does your password have at least one lower case/small letter?\n").lower()
if lower == "yes":
	low_case = True
	count +=1
	
num = input("Does your password have at least one number/digit?\n").lower()
if num == "yes":
	have_num = True
	count +=1
	
if count >= 3:
	print("This is a suitable password.")
else:
	print("This is not a suitable password")	
	

	



