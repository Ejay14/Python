#Author: Jabulani Mavodze
#Task L1T07
#Compulsory Task 1
#Date :27 January 2022

#This block of code requests user input and it then computes the age 
year = int(input("Please enter the year you were born:\n"))
age = 2022 - year

#This block of code checks if age is greater or equals to 18
if age >= 18:
	print("Congrants you are old enough")
else :
	print("Sorry you are still a baby")	
