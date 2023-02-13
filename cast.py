#Author: Jabulani Mavodze
#Task 3
#Compulsory Task 2
#Date :14 January 2022

#This block of code requests user inputs
fav_rest = input("Please enter your favourite restaurant:")
int_fav = int(input("Please enter your favourite number:"))

#This block of code prints out the inputs from the user
print(fav_rest)
print(int_fav )

#fav_rest = int(fav_rest)
#This line of code yields an error, 
#since we are trying to convert a string of characters into integers
#this cant be done since the fucntion int() expects digits instead of string character.
#A string of digits would not yield an error since it will the correct argument for the function. 
