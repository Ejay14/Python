#Author: Jabulani Mavodze
#Task L1T10
#Compulsory Task 3
#Date :03 February 2022

##This block of code requests user input, the user must enter the minutes of each event.
swimming = int(input("Please enter the minutes it took to complete the event (swimming):\n"))
cycling = int(input("Please enter the minutes it took to complete the event (cycling):\n"))
running = int(input("Please enter the minutes it took to complete the event (running:\n"))
Total_Time = swimming+cycling + running

#This block of code determines the award to be given using conditional statements and the total time,
#after adding all the minutes from each event.
if Total_Time < 100:
	print(f"Your total time is: { Total_Time } minutes , thus your award is the Provincial Colours.")
	
elif Total_Time > 100 and Total_Time <= 105:
	print(f"Your total time is: { Total_Time } minutes, thus your award is the Provincial Half Colours.")
	
elif Total_Time > 105 and Total_Time <= 110:
	print(f"Your total time is: { Total_Time } minutes, thus your award is the Provincial Scroll.")
	
else:
	print(f"Your total time is: { Total_Time } minutes, thus No award.")


