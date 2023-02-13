#Author: Jabulani Mavodze
#Task L1T07
#Compulsory Task 2
#Date :27 January 2022

name = input("Please enter your full name:\n")

if name == " ":
	print("You haven’t entered anything. Please enter your full name.")
	
elif len(name) != 0 and len(name) < 4:
	print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
	
elif len(name) > 25:
	print("You have entered more than 25 characters. Please make sure thatyou have only entered your full name.")
	
else:
	print("Thank you for entering your name.")
		
	
