#Author: Jabulani Mavodze
#Task L1T25
#Compulsory Task 1
#Date :07  March 2022

#This function calculates a sum in a given array recursively.
def sum(arr,num):
	#base case
	 if len(arr) == 1:
	 	return arr[0]
	 else:
	 	return arr[0] + sum(arr[1:num],num)
	  

#This block of code declares and initialise an array and the variable 'nums' , and procced to populate the array using a while loop.        
array = []       
nums = input("Please enter integers to be summed up and enter (done) when you are done:\n").lower()
while nums!= "done":
	
	if  nums != "done":
		array.append(int(nums))
	nums = input().lower()
		
#This block of code request user input, the user will enter an index of an array which wiil use to sum up to inclusive.
up_to = int(input("Please enter an index we sholud add up to:\n"))
if up_to < len(array):
	up_to +=1	
	print(sum(array,up_to))
else:
	print("Error!")
