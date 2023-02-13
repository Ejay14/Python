#Author: Jabulani Mavodze
#Task L1T22
#Compulsory Task 3
#Date :03 March 2022

#This block of code declares the array 'content' and opens the file 'input.txt' to read content.
content = []
with open('input.txt','r+') as f:
	content = f.readlines()

#This function returns a minimun number in a list.	
def Min ():
	string = content[0]
	for i in string:
		if i.isdigit():
			ind = string.index(i)
			tmp = string[ind:]
			tmp_list = tmp.split(",")
			break
	return min(tmp_list)

#This function returns a maximun number in a list.	
def Max ():
	string = content[1]
	for i in string:
		if i.isdigit():
			ind = string.index(i)
			tmp = string[ind:]
			tmp_list = tmp.split(",")
			break
	return max(tmp_list)

#This function return an average for the numbers in a list	
def Avg ():
	string = content[2]
	for i in string:
		if i.isdigit():
			ind = string.index(i)
			tmp = string[ind:]
			tmp_list = tmp.split(",")
			tmp_list = list(map(int,tmp_list))
			break
	return sum(tmp_list)/len(tmp_list)

#This block of code opens/creates the file 'output.txt' and calls the fuctions above and the writes to the file. 
with open('outputs.txt','a') as f:
	ans1 = Min()
	ans2 = Max()
	ans3 = Avg()
	f.write(str(f"The min of [1,2,3,4,5,6] is {ans1}\n"))
	f.write(str(f"The max of [1,2,3,4,5,6] is {ans2}"))
	f.write(str(f"The avg of [1,2,3,4,5,6] is {ans3}"))


