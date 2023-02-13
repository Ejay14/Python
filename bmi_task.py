#Author: Jabulani Mavodze
#Task L1T09
#Compulsory Task 2
#Date :30 January 2022

#This block of code requests user input and then declares the variables weight,height and state.
weight = float(input("Please enter your weight in (kg):\n"))
height = float(input("Please enter your height in (m):\n"))
state = "normal"

#This line computes the bmi of the user using their weight and height.
bmi = round((weight)/(height*height),3)

#This block of code determines the state of the user based on their BMI.
if bmi  > 30.0:
	state = "obese"
elif bmi >= 25.0:
	state = "overweight"
elif bmi >= 15.5:
	state = "normal"
else:
	state = "Underweight"
	
print(f"Your BMI is: {bmi} ,thus you are {state}.")	
	
