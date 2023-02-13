#Author: Jabulani Mavodze
#Task L1T15
#Compulsory Task 2
#Date :12 February 2022 

#This line of code requests user input, the user must enter a sentence, and then the sentence is split using the function split() with an empty string delimeter.
sentence = input("Please enter a sentence:").split(" ")

#This block of code , uses a for loop to print every word of the sentence entered  on a different line.
for i in range(len(sentence)):
	print(sentence[i])
