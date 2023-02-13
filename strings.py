#Author: Jabulani Mavodze
#Task 3
#Compulsory Task 1
#Date :14 January 2022
#Corrected version

#This block of code,declares the variable hero and uses the string function str.upper() to attain the new string "SUPER MAN" with upper cases.
hero = "Super Man"
hero = hero.upper()

#This block of code manipulates the new string "SUPER MAN" by using string slicing get each character of the string and concatenate it with a character
sChar1 = hero[0:1]+ "^"
sChar2 = hero[1:2]+ "^"
sChar3 = hero[2:3]+ "^"
sChar4 = hero[3:4]+ "^"
sChar5 = hero[4:5]
sChar6 = hero[5:6]
sChar7 = hero[6:7]+ "^"
sChar8 = hero[7:8]+ "^"
sChar9 = hero[8:9]

#This block of code creates the desired string "S^U^P^E^RM^A^N" by using string concatenation and prints it out.
word = sChar1+sChar2+sChar3+sChar4+sChar5+sChar6+sChar7+sChar8+sChar9
print(word)

