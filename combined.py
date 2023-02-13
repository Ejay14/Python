#Author: Jabulani Mavodze
#Task L1T18
#Compulsory Task 1
#Date :22 February 2022 

from random import seed
from random import randint
seed(1)

#This block of code, declares three lists 'numbers_1', 'numbers_2' and 'numbers_3'. 
numbers_1 = []
numbers_2 = []
numbers_3 = []

#This block of code, opens a file called 'numbers1.txt' to write 20 sorted random generated integers.
with open('numbers1.txt','w') as f:

	for _ in range(20):
		value = randint(0, 100)
		numbers_1.append(value)
	numbers_1.sort()
	
	for i in numbers_1:	
		f.write(str(i)+"\n")
#This block of code, opens a file called 'numbers2.txt' to write 20 sorted random generated integers.		
with open('numbers2.txt','w') as f:

	for _ in range(20):
		value = randint(0, 100)
		numbers_2.append(value)
	numbers_2.sort()
	
	for i in numbers_2:	
		f.write(str(i)+"\n")
#This block of code, opens a file called 'all_numbers.txt' , 
#and then it opens the two above mentioned files 'numbers1.txt' and 'numbers2.txt' to read their content so that it can write their content into the file 'all_numbers'.	
with open('all_numbers.txt','w') as f:

	with open('numbers1.txt','r+') as f1:
		for line in f1:
			content = line.strip("\n")
			numbers_3.append(int(content))
			
	with open('numbers2.txt','r+') as f2:
		for line in f2:
			contents = line.strip("\n")
			numbers_3.append(int(contents))
			
	numbers_3.sort()
	for t in numbers_3:	
		f.write(str(t)+"\n")
		
	
