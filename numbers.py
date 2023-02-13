#Author: Jabulani Mavodze
#Task 4
#Compulsory Task 1
#Date :16 January 2022

#This block of code requests user inputs.
int_fav1 = int(input("Please enter integer one:"))
int_fav2 = int(input("Please enter integer two:"))
int_fav3 = int(input("Please enter integer three:"))

#This block of code performs basic math arithmatics.
Sum = int_fav1 + int_fav2 + int_fav3
diff = int_fav1 - int_fav2 
mult = int_fav1*int_fav2
av = (int_fav1 + int_fav2 + int_fav3)/int_fav3
av = round(av,2)

#This block of code prints out the answers of the basic math arithmatics computed.
print(f"The sum of all numbers is: {Sum}")
print(f"The first number minus the second number is: {diff}")
print(f"The third number multiplied by the first number is:{mult}")
print(f"The sum of all three numbers divided by the third number is: {av}")



