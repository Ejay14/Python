#Author: Jabulani Mavodze
#Task L1T08
#Compulsory Optional Bonus Task 
#Date :29 January 2022

#This block of code declares the wage variables for the saleperson and manager
wage_sales = 2000.00
wage_man = 40.00

#This block of code requests user input in onder to distiguish between a salesperso and a manager.
title = input("Are you a salesperson or a manager:\n").lower()

#This block of code computes the monthly wage of a salesperson and a manager.
if title == "salesperson":
 	gross_sales = float(input("Please enter your gross sales:\n"))
 	wage_sales += gross_sales*0.08
 	print(f"Your monthly wage is: {wage_sales}")
else:
 	hours = int(input("Please enter the numbers of hours worked this month:\n"))
 	wage_man += hours*40.00
 	print(f"Your monthly wage is: {wage_man}")
 		

	

