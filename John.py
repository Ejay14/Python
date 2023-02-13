#Author: Jabulani Mavodze
#Task L1T16
#Compulsory Task 2
#Date :14 February 2022

#This block of code,requests user input the user enters a name(strings),it also declares a list 'names'.
name = input("Enter your name:")
names = []

#This block of code  adds incorrect names into the list 'names' using a while loop and terminates when the user enters the string 'John', 
#and then it prints out the contents of the list 'names'.
while name != "John":
	names.append(name)
	name = input("Enter your name:")
	
print(f"Incorrect names: {names}")
