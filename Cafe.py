#Author: Jabulani Mavodze
#Task L1T20
#Compulsory Task 1
#Date :01 March 2022


#This block of code declares and initialises an array 'menu', two dictionaries 'stock' and 'price' as well a the variable 'Total'.
menu = ["Jelly babies","Coffee","Cold drink","Bread"]

stock = {1 : "Jelly babies",
	 2 : "Coffee",
	 3 : "Cold drink",
	 4 : "Bread" 
	}

price = {"Jelly babies" : "R13",
	 "Coffee" : "R10",
	 "Cold drink" : "R22",
	 "Bread" : "R17"
	}
	
Total = 0	


#This block of code uses a for loop to calculate the totall stock worth using elements in the array 'menu' and from the dictionary 'price'.
for i in menu:
	content = int((price.get(i)).strip("R"))
	Total+=content

print(f"The total stock worth in the cafe is: R{Total}")
