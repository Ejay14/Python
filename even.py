#Author: Jabulani Mavodze
#Task L1T12
#Compulsory Task 1
#Date :07 February 2022

#This block of code requests user input,the user is required to enter an integer,
# it aslo declares and instatiate the variabele count to 1.
num = int(input("Please enter an integer:\n"))
count = 1

#This block of code , prints all even numbers from 1 up to the integer entered by the user using a while loop.
while count <= num:
	if count%2 ==0:
		print(count)
	count += 1	
