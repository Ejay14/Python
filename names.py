#Author: Jabulani Mavodze
#Task L1T12
#Compulsory Task 2
#Date :07 February 2022

#This block of code requests user input,the user is required to enter names(string) of all pupils in a class ,
# it aslo declares and instatiate the variabele count to 1.
names  = input("Please enter names of all pupils in a class:\n")
count = 0

#This block of code, repetitively take names(string) of all pupils in a class and counts them and then prints the the total.
while names!= "stop":
	names  = input()
	count += 1

print(f"The number of pupils in this class is :{count}")	

