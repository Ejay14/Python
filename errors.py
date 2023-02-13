# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#Compilation error: The syntax is wrong missing parentheses in call to 'print',thus we need to insert parenthesis ().
print ("Welcome to the error program")

#Compilation error: The syntax is wrong missing parentheses in call to 'print',thus we need to insert parenthesis ().
#Compilation error: incorrect space indentation, needs to be in line with print 
print( "\n")

#Compilation error: incorrect space indentation, needs to be in line with print 
#Runtime error: name 'ageStr' is not defined, the line uses double equals to sign,
# which is to compare and not assign.
ageStr ="24 years old" #I'm 24 years old.

#Runtime error: invalid literal for int(), the line is trying to convert characters into integers,
#the function int() accepts string digits only,we can use the substring function to get the digit part of the string.
age = int(ageStr[0:3:1])

#Runtime error: We can only concatenate str (not "int") to str, we can use string formatting to get the value of age.
print(f"I'm {age} years old.")


three = "3"

#Compilation error: incorrect space indentation, needs to be in line with 'three' and 'print'
#Runtime error: unsupported operand type(s) for +: 'int' and 'str', the line is trying to add different types a string and an integer,
# thus we should convert the string into an integer using int() so that we can perform the addition
answerYears = age + int(three)

#Compilation error: The syntax is wrong missing parentheses in call to 'print',thus we need to insert parenthesis ().
#LogicError: answerYears is not supposed to under the quotation marks,we can use string formatting to remedy this.
print (f"The total number of years:{answerYears}")

#Compilation error: name 'answer' is not defined, the variable answer is not completehence we have to write it in full i.e answerYears.
#LogicError: This line of code does not take into account the 6 months part of the statement,
# thus the logic is wrong, hence we need to add the value 6.
answerMonths = answerYears*12 + 6
#compilation error:We can use string formatting to fix this.
#Runtime error: We can only concatenate str (not "int") to str, we can use string formatting to get the value of answerMonths.
print (f"In 3 years and 6 months, I'll be {answerMonths} months old")

#HINT, 330 months is the correct answer

