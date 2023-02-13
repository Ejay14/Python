# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.
 
name = "Tim"

#Compilation error; incorrect space indentation, needs to be in line with 'name' and 'age'
surname = " Jones"
age = 21

#Runtime error; 'age' needs to be indented with str() 
#Compilation error; 'is' is under the wrong syntax, needs to be within " ",or we can use string formatiing.
fullMessage = f"{name} {surname} is {age} years old"

# Logical error; fullMessage does not have appropriate spacing requiring: + " " +,or we can use string formatiing.
print (fullMessage)
