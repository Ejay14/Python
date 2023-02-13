#Author: Jabulani Mavodze
#Task 3
#Compulsory Task 2
#Date :14 January 2022
#Corrected version

#This block of code declares the variable sentence 
#Strips the exclamation mark from the string by using the str.strip() function 
#It then changes the string from lower cases to upper cases using the str.upper() function. 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"
sentence = sentence.replace("!"," ")
print(sentence)
sentence = sentence.upper()
print(sentence)

#This block of code splits the string by using the str.split() function sing the empty space delimeter. 
#since using the split function yields an array,
#I used indexing to access every word on the array from the tail of the of the array so that I can print it in reverse. 
nWord = sentence.split(" ")
sChar1 = nWord[8]
rev1 = sChar1[::-1]+ " "
sChar2 = nWord[7]
rev2 = sChar2[::-1]+ " "
sChar3 = nWord[6]
rev3 = sChar3[::-1]+ " "
sChar4 = nWord[5]
rev4 = sChar4[::-1]+ " "
sChar5 = nWord[4]
rev5 = sChar5[::-1]+ " "
sChar6 = nWord[3]
rev6 = sChar6[::-1]+ " "
sChar7 = nWord[2]
rev7 = sChar7[::-1]+ " "
sChar8 = nWord[1]
rev8 = sChar8[::-1]+ " "
sChar9 = nWord[0]
rev9 = sChar9[::-1]+ " "

nWord2 = rev1 + rev2 + rev3 + rev4 + rev5 + rev6 + rev7 + rev8 + rev9
print(nWord2)

