#Author: Jabulani Mavodze
#Task L1T17
#Compulsory Task 
#Date :22 February 2022 

#This block of code, declares two lists 'names' and 'dates, these two lists will store names and birthdays respectively from the data of the given file.
names = []
dates = []

#This block of code ,opens the file DOB.txt  and reads the contents using the function readlines(), and it also seperates the name and birthdate from each line and then it stores them on the declared lists above.
with open('DOB.txt','r+') as f:
	newContents = f.readlines()

	for i in range(len(newContents)):
		line = newContents[i].strip("\n")
		for j in line:
			if j.isdigit():
				
				index = line.index(j)
				
				names.append(line[:index])
				
				dates.append(line[index:])
				
				break
#This block of code prints outs the content of the two  lists .
	print("Name:")			
	for t in names:		
		print(t)
		
	print()
	print("Birthdate:")
	for k in dates:
		print(k)

