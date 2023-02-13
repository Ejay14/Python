#Author: Jabulani Mavodze
#Task L1T26
#Compulsory Task 1
#Date :09  March 2022

					
#This block of code requsets user input and then procced to compute math arithmatics if the input is correct.
while True:
	try:
		choice = input("What would you like to do - enter numbers/read file:\n").lower()
	
		if choice == "enter numbers":
			
			with open('equations.txt','a') as f:
			
				while True:
                                       #This block of code makes sure only numbers are accepted as input.
					while True:
						try:
							num1 = float(input("Please enter two numbers:\n"))
							num2 = float(input(""))
							break
						except ValueError:
							print("Oops! That was not a valid number. Try again...")
								
					operation = input("please enter an operation from the following (+ , - , x , /):\n")
					
			               #This block of code performs addition and then displays the results.
					if operation == "+":
						ans = num1 + num2
						ans = str(f" {num1} + {num2} = {ans}\n")
						print(ans)
						f.write(str(f" {num1} + {num2}\n"))
						op = input("Do you want to continue entering numbers yes or no:\n").lower()
						if op == "no":
							break
					#This block of code performs subtration and then displays the results.		
					elif operation == "-":
						ans = num1 - num2
						ans = str(f"{num1} - {num2} = {ans}\n")
						print(ans)
						f.write(str(f" {num1} - {num2}\n"))
						op = input("Do you want to continue entering numbers yes or no:\n").lower()
						if op == "no":
							break
					#This block of code performs multiplication and then displays the results.
					elif operation == "x":
						ans = num1 * num2	
						ans = str(f"{num1} x {num2} = {ans}\n")
						print(ans)
						f.write(str(f" {num1} x {num2}\n"))
						op = input("Do you want to continue entering numbers yes or no:\n").lower()
						if op == "no":
							break
							
					#This block of code performs division and then displays the results.
					elif operation == "/":
						ans = num1 / num2	
						ans = str(f" {num1} / {num2} = {ans}\n")
						print(ans)
						f.write(str(f" {num1} / {num2}\n"))
						op = input("Do you want to continue entering numbers yes or no:\n").lower()
						if op == "no":
							break
					else:
						print("Error!: Please enter an operation from the following (+ , - , x , /):\n")
						
			op = input("Do you want to quit yes or no:\n").lower()
			if op == "yes":
				print("Goodbye")
				break
				
		elif choice == "read file":
		#This block of code fetches content from the given file and  then displays it.
			File = input("Please enter the name of the file:\n")
			while True:
				try:
					with open(File,'r+') as f:
						lines = f.readlines()
						if len(lines) > 0:
							for line in lines:
								print(line)
						else:
							print("File is empty")
						break
				except FileNotFoundError:
					print("Error:File does not exist!")
					File = input("Please enter the name of the file:\n")
					
			op = input("Do you want to quit yes or no:\n").lower()
			if op == "yes":
				print("Goodbye")	
				break	
				
		else:
			print("Oops - incorrect input")
		
	except Exception:
			print("Error, file does not exist.")
			File = input("Please enter the name of the file:\n")


