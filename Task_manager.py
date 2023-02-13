'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''
import fileinput
import sys
#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
user_input = []
file_input = []
content = []
lines = []
count1 = 0
count2 = 0
count = True

with open('user.txt','r+') as f:
	content = f.readlines()
if len(content) == 1:
	for line in fileinput.input('user.txt', inplace=1):
		if "admin, adm1n" in line:
		    line = line.replace("admin, adm1n","admin, adm1n\n")
		sys.stdout.write(line)

with open('user.txt','r+') as f:
	contents = f.readlines()
	file_input = contents
	
	
username = input("Please enter your username:")
password = input("Please enter your password:")
user_input.append(f"{username}, {password}\n")
		
while count:
	
	if user_input[0] in file_input:
		count = False
	else:		
		username = input("LogIn Error:Please re-enter your username:")
		password = input("LogIn Error:Please re-enter your password:")
		user_input.remove(user_input[0])
		user_input.append(f"{username}, {password}\n")
		
		
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    #user = (user_input[0]).split(", ")
    if user_input[0] == "admin, adm1n\n":
    	menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
st - View statistics
e - Exit
: ''').lower()
    else:
     	menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my tasks
e - Exit
: ''').lower()
	

    if menu == 'r':	
    	
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

        new_username = input("Please enter your username:")
        new_password = input("Please enter your password:")
        confirm_password = input("Please confirm your password:")
        while  new_password != confirm_password:
        	confirm_password = input("Erorr password mismatch: Please confirm your password:")
        with open('user.txt','a') as f:
        	f.write(f"{new_username}, {new_password}\n")
        		
           		
    elif menu == 'a':
        
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
       	with open('tasks.txt','r+') as f:
       		lines = f.readlines()
       		print(lines)
       	if len(lines)==2:
       		for line in fileinput.input('tasks.txt', inplace=1):
       			if lines[1] in line:
       				line = line.replace(lines[1],lines[1]+"\n")
       			sys.stdout.write(line)
			    	
        ass_username = input("Please enter the username of the assignee:")
        title = input("Please enter the title of the task:")
        description = input("Please enter the description of the task:")
        due_date = input("Please enter the due date of the task in this format(day month year) e.g 10 Feb 2020:")
        current_date = input("Please enter the current date in this format(day month year) e.g 10 Feb 2020:")
        with open('tasks.txt','a') as f:
        	done = input("Is the task done (Yes) OR (No):").lower()
        	f.write(f"{ass_username}, {title}, {description}, {due_date}, {current_date}, {done}\n")
              	
    elif menu == 'va':
        
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        with open('tasks.txt','r+') as f:
         	for line in f:
         		content = line.split(", ")
         		print("Task:              ",content[1])
         		print("Assigned to:        ",content[0])
         		print("Date assigned:     ",content[4])
         		print("Due date:          ", content[3])
         		print("Task complete      ", content[5])
         		print("Task description:  ",content[2])
         			

    elif menu == 'vm':
        
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        user = (user_input[0]).split(", ")
        with open('tasks.txt','r+') as f:
        	for line in f:
        		Content = line.split(", ")
        		if user[0] == Content[0]:
        			print("Task:              ",Content[1])
        		else:
       				print("Error not the right the user!")
    elif menu == "st":
    	with open('tasks.txt','r+') as f:
        	for line in f:
        		Content = line.split(", ")
        		if Content[0] != "":
        			count1 += 1
        		if Content[1] != "":
        			count2 += 1
       		print(f"The total number of users is: {count1}")
       		print(f"The total number of tasks is: {count2}")
        	
    	 			
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    else:
        print("You have made a wrong choice, Please Try again")
