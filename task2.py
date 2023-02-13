#Author: Jabulani Mavodze
#Task L1T10
#Compulsory Task 2
#Date :03 February 2022

import math 

#This line of code requests user input, the user must enter a shape.
shape = input("Please enter the shape of the building i.e square,rectangular or round:\n")

#This block of code calculates the area of the shape provided by the user,
#It also request specific dimesions in order to compute the specific areas.
if shape == "square":
	length = float(input("Please enter the length of the square:\n"))
	Area = length**2
	print(f"The area of the square is : {Area}")
elif shape == "rectangular":
	length = float(input("Please enter the length of the rectangular:\n"))
	width = float(input("Please enter the width of the rectangular:\n"))
	Area = lenght*width
	print(f"The area of the rectangular is : {Area}")
else:
	radius =  float(input("Please enter the radius of the circle:\n"))
	Area = round((math.pi)*(radius**2),2)
	print(f"The area of the circle is : {Area}")
