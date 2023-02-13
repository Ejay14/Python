#Author: Jabulani Mavodze
#Task L1T10
#Compulsory Task 1
#Date :03 February 2022

#This block of code declares and initialises the variables num1,num2 and num3.
num1 = 25
num2 = 2
num3 = 53

#This block of code ,uses conditinal statements to check if num1 is greater than num2.
#And it also checks if num1 is an even number.
if num1 > num2:
	print(f"The large value is: {num1}")
else:
	print(f"The large value is: {num2}")	
	
if num1%2 == 0:
	print("num1 is an even number")
else:
	print("num1 is an odd number")

#This block of code, sorts the values of the declared variables in ascending order using conditional statements.	
smallest = 0
middle = 0
biggest = 0
 
if num1 < num2 and num1 < num3:
  if (num2 > num3):
       smallest = num1
       biggest = num2
       middle = num3
       print(f"{smallest},{middle},{biggest}")
if num1 < num2 and num3 < num1:
  if (num2 < num3):
       smallest = num1
       middle = num2
       biggest = num3
       print(f"{smallest},{middle},{biggest}") 
if num1 > num2 and num3 > num1:
  if (num2 < num3):
       middle = num1
       smallest = num2
       biggest = num3
       print(f"{smallest},{middle},{biggest}")
if num1 < num2 and num3 < num1:
  if (num2 > num3):
       middle = num1
       biggest = num2
       smallest = num3
       print(f"{smallest},{middle},{biggest}") 
if num1 > num2 and num1 > num3:
  if (num3 > num2):
       biggest = num1
       middle = num3
       smallest = num2
       print(f"{smallest},{middle},{biggest}") 
if num1 > num2 and num1 > num3:
  if (num2 > num3):
       biggest = num1
       middle = num2
       smallest = num3
       print(f"{smallest},{middle},{biggest}")
    


