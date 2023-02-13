#Author: Jabulani Mavodze
#Task L1T15
#Compulsory Task 1
#Date :12 February 2022 

#This block of code requests user enter input ,the user is required to enter a word(string).It also declares and instatiate the variable New_word to an empty string.
#lastly it assigns size if the entered word to the variable length.
word = input("Please enter a word:")
New_word =""
length = len(word)

#This block of code creates a new word where the alternate character is in lowercase,using a for loop and conditional statements.
#The logic is that we check the index of a character if it is an even number ,if true we switch the character into an uppercase character then we concatenate it to the variable New_word.
for i in range(length):
	if i%2 == 0:
		New_word = New_word + word[i].upper()
	else:
		New_word = New_word + word[i].lower()
	
print(New_word)


