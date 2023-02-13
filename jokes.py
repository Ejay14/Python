#Author: Jabulani Mavodze
#Task L1T21
#Compulsory Task 2
#Date :01 March 2022

from random import seed
from random import randint
seed(1)

#This block of code declares and intialises the array 'jokes'.
jokes = ["My wife told me to stop impersonating a flamingo. I had to put my foot down.","I went to buy some camo pants but couldn’t find any.","I failed math so many times at school, I can’t even count."," I used to have a handle on life, but then it broke."," I was wondering why the frisbee kept getting bigger and bigger, but then it hit me.","I heard there were a bunch of break-ins over at the car park. That is wrong on so many levels.","I want to die peacefully in my sleep, like my grandfather… Not screaming and yelling like the passengers in his car.","When life gives you melons, you might be dyslexic.","Don’t you hate it when someone answers their own questions? I do.","It takes a lot of balls to golf the way I do."]



#this block of code requsets user input ,and then it generates and prints a random joke from the array.
ans = input("You want to here a joke (yes) or (no):\n").lower()
while ans == "yes":
	index = randint(0,10)
	print(jokes[index])
	ans = input("You want to here a joke (yes) or (no):\n").lower()
	






