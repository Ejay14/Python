#Author: Jabulani Mavodze
#Task L1T09
#Compulsory Task 1
#Date :30 January 2022

#This line of code requests user input and then declares the variable age.
age = int(input("Please enter your age :\n"))
 
#This block of code determines if the user is old enough using control structures. 
if age >= 18:
	print("You are old enough!")
elif age > 16 and age < 18:
	print("You are almost there")	 
else:
	print("You are too young!")	

