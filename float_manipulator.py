#Author: Jabulani Mavodze
#Task L1T21
#Compulsory Task 1
#Date :03 March 2022

import math

#This block of code requests user input, declares an array 'deci' and the variable 'Total' ,
#and the it uses a for loop to sum up the numbers entered by the user.
print("Please enter 10 float/decimal numbers:")
deci = []
Total = 0.0
for i in range(10):

	number = float(input())
	Total+= number
	deci.append(number)
	

#This block of code prints the sum of the numbers in the array, the maximum vale in the array,
#the minimum value in the array, the indexes of the maximum and minimum values and lastly the average ofthe numbers in the array.
print(f"The total of all numbers is: {Total}")
print(f"The maximum number on the list is: {max(deci)}")
print(f"The index of the maximum number on the list is: {deci.index(max(deci))}")
print(f"The index of the manimum number on the list is: {deci.index(min(deci))}")
print(f"The average of the numders in the list is: {round(Total/10,2)}")
