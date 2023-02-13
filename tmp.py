num1 = 0
num2 = 0
ans = 0

choice = input("What would you like to do - enter numbers/read file:\n").lower()
print(choice)
if choice == "enter number":
	try:
		with open('equations.txt','a') as f:
			print("in")
	
	except Exception:
		print("Error, file does not exist.")
