
#This block of code takes in user input for the variables 'name','age','hair_colour' and 'eye_colour'.
name = input("Please enter your name:\n")
age = eval(input("Please enter your age:\n"))
hair_colour = input ("Please enter your hair colour:\n")
eye_colour = input("Please enter your eye colour:\n")

#This is a class defination for the parent class 'Adult'.
#The class has a contructor that initialises four variables, 'name','age','hair_colour' and 'eye_colour'.
#The class has a function 'can_drive()'.
class Adult:
	
	def __init__(self,name,age,hair_colour,eye_colour):
		self.name = name
		self.age = age
		self.hair_colour = hair_colour
		
	def can_drive(self):
		print(f"{self.name} is old enough to drive")
		
#This is a class defination for the subclass class 'Child'.
#This class inherits from the 'Adult' class as shown by the call to the super function in the contructor.
#The class overrides the method 'can_drive'.	
class Child(Adult):
	
	
	def __init__(self,name,age,hair_colour,eye_colour):
		super().__init__(name,age,hair_colour,eye_colour)
		
	def can_drive(self):
		print(f"{self.name} is too young to drive")
#This block of code determines which object to create based on the user input and call the correct 'can_drive()' function.		
if age >= 18:
	person = Adult(name,age,hair_colour,eye_colour)
	person.can_drive()
else:
	person = Child(name,age,hair_colour,eye_colour)
	person.can_drive()
