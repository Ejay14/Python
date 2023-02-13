"""
Compulsory Task 1: 
------------------

Use the code provided copied to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Woodstock, Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

On a side note, this task covers single inheritance. multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course
"""
#This is a class defination for the parent class 'Course':
#The class has a contructor that initialises three variables, 'name','contact' and 'location'
#The class has two functions 'contact_details()' and 'location_details()',
#that print contact details and location details respectively.
class Course:
   
    def __init__(self):
    	self.name = "Fundamentals of Computer Science"
    	self.contact_website = "www.hyperiondev.com"
    	self.location = "Woodstock, Cape Town"
    	
    def contact_details(self):
        print(f"Please contact us by visiting {self.contact_website}")
        
    def location_details(self):
    	print(f"Please visit us at our head office in {self.location}")
  
#This is a class defination for the subclass class 'OOPCourse'.
#This class inherits from the 'Course' class as shown by the call to the super function in the contructor,
#and also adds two variables 'description' and 'trainer'.
#The class has two new function 'trainer_details()' and 'show_course_id()", 
#that print the trainer's details and the course id.
class OOPCourse(Course):
	
	def __init__(self):
		super().__init__()
		self.description = "OOP Fundamentals"
		self.trainer = "Mr Anon A. Mouse"
		
	def trainer_details(self):
		print(f"This course is about {self.description} and the trainer is {self.trainer}")
	
	def show_course_id(self):
		print("The course ID nmuber is : #123456")
		
		
#This block of code create an object using the child class and make a call to the function 'contact_details()'
#a method from the parent class this is possible due to inheritance(the call of the super function in the cotructor). 
#Calls to functions from the sub class are also made.		
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
		
		
		
	
