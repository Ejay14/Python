#Author: Jabulani Mavodze
#Task L1T15
#Compulsory Task 3
#Date :12 February 2022

sentence = input("Please enter a sentence:\n")
dis=input("Please enter characters(seperated by a comma),you would like to make disappear:\n").split(",")

for i in range(len(dis)):
	sentence = sentence.replace(dis[i],"")

print(sentence)

