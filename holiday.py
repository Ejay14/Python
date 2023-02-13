#Author: Jabulani Mavodze
#Task L1T22
#Compulsory Task 2
#Date :03 March 2022

#This function computes the hotel cost given the number of nights a client will stay in the hotel.
def hotel_cost (nights):
	return 350*nights
	
#This function computes the plane cost given the city.	
def plane_cost (city):
	if city == "durban":
		return 500
	elif city == "johannesburg":
		return 850
	elif city == "gqeberha":
		return 500
	elif city == "cape town":
		return 950
	else:
		return 450
#This function computes the car rental cost given the amount of days the client is going to use the car.
def car_rental (days):
	return 150*days

#This function the computes the total cost of the entire holiday package.
def holiday_cost (nights,city,days):
	return plane_cost (city) + car_rental (days) +hotel_cost (nights )
	
	
nights = int(input("How many nights are going to stay for your holiday:\n"))
city = input("Which city do you want to spend your holiday in:\n").lower()
days = int(input("How many days are going to stay for your holiday:\n"))
print(f"The total cost for yoyr holiday is: R{holiday_cost (nights,city,days)}")
