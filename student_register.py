#Author: Jabulani Mavodze
#Task L1T18
#Compulsory Task 1
#Date :22 February 2022 


#This block of code, creates a file 'reg_form, and then it writes to it using the function write.
#It write ID numbers of students using a for loop.
with open('reg_form.txt','w') as f:
	num = int(input("Please enter the number of students:"))
	for i in range(num):
		id_num = input("Please enter your ID number:")
		f.write(id_num+"\n")
	
		
		
