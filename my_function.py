#Author: Jabulani Mavodze
#Task L1T22
#Compulsory Task 1
#Date :03 March 2022

#This function prints days of the week.
def days ():
	Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	print("Days of the week:")
	for i in Days:
		print(i)
		
#This function takes in a sentence and replace 	every second word with the word 'Hello'.	
def sentence (word):
	content = word.split(" ")
	newWord = content[0]
	for i in range(len(content)):
		if i%2 != 0 :
			content[i] = "Hello"
	for j in range(1,len(content)):
		newWord = newWord +" "+ content[j]
	print(newWord)

#This block of code calls the two functions created above.			
days()
word = input("Please enter a sentence:\n")
sentence(word)		
