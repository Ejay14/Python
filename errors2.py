# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#Compilation error; name 'Lion' is not defined,wrong syntax the value 'Lion' needs to be within " " . marks.
animal = "Lion"
#Compilation error; incorrect space indentation, needs to be in line with 'animal' and 'number_of_teeth'
animal_type = "cub"
number_of_teeth = 16

#Compilation error; 'is' is under the wrong syntax, needs to be within " " .
#Runtime error; 'age' needs to be indented with str() or we can use string formatiing.
#Logical error; fullMessage does not have appropriate spacing requiring: + " " + or we can use string formatting.
full_spec = f"This is a {animal}.It is a {number_of_teeth} and it has {animal_type} teeth"
#Compilation error: The syntax is wrong missing parentheses in call to 'print'.
print (full_spec)

