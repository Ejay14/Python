#Author: Jabulani Mavodze
#Task L1T12
#Compulsory Task 3
#Date :07 February 2022

#This block of code requests user input,the user is required to enter an integer,
# it aslo declares and instatiate the variabeles count  and total to 0.
num = int(input("Please enter an integer:\n"))
count = 0
total = 0

#This block of code, calculates the average of the numbers entered using a while loop,
#in the while lopp we add num to total and then compute the average once the while loop terminates and print it.
while num!=-1:
	num = int(input("Please enter an integer:\n"))
	if num > -1:
		total += num
		count += 1
	
average = round(total/count,0)
print(f"The average entered is :{average}")
