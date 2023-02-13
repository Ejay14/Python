#Author: Jabulani Mavodze
#Task L1T20
#Compulsory Task 3
#Date :01 March 2022

word = input("Please enter a word:\n")

count = {}

for i in word:
	if i in count:
		continue
	else:
		count[i]= word.count(i)
		
print(count)
