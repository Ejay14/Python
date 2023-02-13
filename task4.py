#Author: Jabulani Mavodze
#Task L1T10
#Compulsory Task 4
#Date :03 February 2022

#This line of code requests user input,the user is required to enter an integer.
num = int(input("Please enter an integer:\n"))

#This block of code uses conditional statements to check, if the integer entered is divisible by 2 and 5.
#It also checks if the integer entered is divisible by 2 or 5.
#It also checks if the integer entered is not divisible by 2 or 5.
if num%2 == 0 and num%5==0:
	print(f"{num} is divisible by 2 and 5")
elif num%2 == 0 or num%5==0:
	print(f"{num} is divisible by 2 or 5")
else:
	print(f"{num} is not divisible by 2 or 5")
