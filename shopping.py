#Author: Jabulani Mavodze
#Task 4
#Compulsory Task 2
#Date :16 January 2022

#This block of code requests the user inputs,
#the user must enter the name of three products.
product1 = input("Please enter product one: ")
product2 = input("Please enter product two: ")
product3 = input("Please enter product three: ")

#This block of code requests the user inputs,
#the user must enter the price of each product.
#Each product must have two decimal values,hence I used the math fuction round().
price1 = float(input("Please enter price of product one: "))
price1 = round(price1,2)
price2 = float(input("Please enter price of product two: "))
price2 = round(price2,2)
price3 = float(input("Please enter price of product three: "))
price3 = round(price3,2)

#This block of code calculates the total of all three products,
# and the average price of the three products.
#It also prints a sentence after performing the calculations.
Total =  price1 + price2 + price3
ave = Total/3
print(f"The Total of {product1}, {product2}, {product3} is R{Total} and the average price of the items are R{ave}")

