
#=====Class Section===========
'''Here I will create a class called Email:
	-The class will have one class variable, 'has_been_read', 'i_spam', 'email_content' and an array 'inbox'.
	-This class has eight function definations.
'''	
class  Email:
#=====Class Variables===========
	inbox = [] 
	has_been_read = False
	is_spam = False
	email_contents = ""
	
	def __init__(self,email_content, from_address):
		self.has_been_read = False
		self.is_spam = False	
		self.email_contents = email_content
		self.from_address = from_address	
		

#This function changes the variable 'has_been_read' to true.
	def mark_as_read(self):
		self.has_been_read = True
		return 	self.has_been_read
		
#This function changes the variable 'is_spam' to true.	
	def  mark_as_spam (self):
		self.is_spam = True
		return 	self.has_been_read
#This function takes contents and email address to make a new Email object.
	def add_email (self,contents,from_address):
		new_Email = Email(contents,from_address)
		(self.inbox).append(new_Email)
			
#This function gets the number of messages stored in the list 'inbox'.	
	def get_count (self):
		return len(self.inbox)
		
#This function gets the email from the specified index.				
	def get_email (self,index):
		(self.inbox[index]).mark_as_read ()
		return (self.inbox[index]).email_contents
		
#This function gets unread messages and then stores them in a list
	def get_unread_emails (self):
		unread = []
		print((self.inbox))
		if len(self.inbox) > 0:
			for i in self.inbox:
				if i.has_been_read == False:
					unread.append(i)
		return unread
	
#This function gets spam messages and then stores them in a list.
	def get_spam_emails (self):
		spams = []
		if len(self.inbox) > 0:
			for i in self.inbox:
				if i.is_spam == True:
					spams.append(i)
		return spams
				
#This function gets the email from the specified index and deletes it.		
	def delete (self,index):
		(self.inbox).pop(index)

#=====Logic Section===========
user_choice	= ""
count = 0
email = Email("null","null")

while user_choice != "quit":
	user_choice = input("What would you like to do - read/mark spam/send/delete/quit?\n")
#Thsi block of code allows the user to view messages from the inbox,they can choose to view unread messages or read.	
	if user_choice == "read":
		msg = input("What would you like to do - view-unread/view-all\n")
		
		if (email).get_count() == 0:
			print ("No emails in the inbox")
		elif msg == "view-all":
			print(f"Enter an index from 0 and less than {email.get_count()}:")
			index = eval(input())
			print(f"From:{(email.inbox[index]).from_address}")
			print((email.inbox[index]).email_contents)
			(email.inbox[index]).mark_as_read()
			while True:
				inp = input("Do you Want to Continue reading emails yes or no?\n")
				if inp == "yes" :
					print(f"Enter an index from 0 and less than {email.get_count()}:")
					index = eval(input())
					print(f"From:{(email.inbox[index]).from_address}")
					print((email.inbox[index]).email_contents)
					(email.inbox[index]).mark_as_read()
				else:
					break
		else:
			arr = email.get_unread_emails()
			print(f"Enter an index from 0 and less than {len(arr)}:")
			index = eval(input())
			print(f"From:{(arr[index].from_address)}")
			print(arr[index].email_contents)
			(arr[index]).mark_as_read()
			while True:
				inp = input("Do you Want to Continue reading emails yes or no?\n")
				if inp == "yes" and index <= len(arr):
					print(f"Enter an index from 0 and less than {email.get_count()}:")
					index = eval(input())
					print(f"From:{(arr[index].from_address)}")
					print((email.inbox[index]).email_contents)
					(email.inbox[index]).mark_as_read()
				else:
					break
#This block of code allows the user to view a message and mark as a spam if it is.
	elif user_choice == "mark spam":
		if len(email.inbox) == 0:
			print ("No emails in the inbox")
		else:
			for i in email.inbox:
				if i.is_spam == False:
					print(f"From:{(i).from_address}")
					print(i.email_contents)
					spam = input("Is it a spam (yes) OR (no):\n").lower()
					if spam == "yes":
						i.mark_as_spam()
						print("Done")
	elif user_choice == "send":
		Content = input("Enter your content:\n")
		re_email = input("Please enter your email address:\n")
		email.add_email(Content,re_email)

#This block of code allows a user to delete a message from the inbox.		
	elif user_choice == "delete":
		if (email).get_count() == 0:
			print ("No emails in the inbox")
		else:
			while True:
				index = eval(input("Please enter index:\n"))
				if index < (email).get_count() and  (email).get_count() != 0:
					email.inbox[index].delete(index)
					print("Done")
				else:
					print(f"Error: Please enter index less than {(email).get_count()}")
#this block of code allows the user to quit the program.					
	elif user_choice == "quit":
			print("Goodbye")
			
	else:
		print("Oops - incorrect input")
		
		
		
