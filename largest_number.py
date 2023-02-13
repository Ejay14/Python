#Author: Jabulani Mavodze
#Task L1T25
#Compulsory Task 2
#Date :07  March 2022

#This function recursively checks and returns the largest number in a given array 
def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        return Max(list[1:]) if Max(list[1:]) > list[0] else list[0]
 
 #This block of code declares and initialise an array, requests user input in order to populate the array and the prints the maximum number in the array.       
array = []       
nums = input("Please enter integers and enter (done) when you are done:\n").lower()
while nums!= "done":
	
	if  nums != "done":
		array.append(int(nums))
	nums = input().lower()
		
print(Max(array))
