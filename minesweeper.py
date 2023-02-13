#Author: Jabulani Mavodze
#Task L1T24
#Compulsory Task 1
#Date :05 March 2022

#This line of code declares and initialises a 2D array 'grid'
grid = [["-", "-", "-", "#", "#"],
	["-", "#", "-", "-", "-"],
	["-", "-", "#", "-", "-"],
	["-", "#", "#", "-", "-"],
	["-", "-", "-", "-", "-"] ]

#This function uses the two functions 'isValid()' and 'isMine()' to return a grid where,
#each dash is replaced by a digit , indicating the number of mines immediately ajacent to the spot.
def mines (lists) :
	rows = len(lists)
	for row in range (rows):
		cols = len(lists[row])
	for i in range (rows):
		for j in range(cols):
			if lists[i][j] != "#":
				lists[i][j] = adjacent_Count(i,j,lists)
			
	return lists

#This function checks if an element is not out of bounds. 
def isValid (row,col):
	return (row >= 0) and (row < 5) and (col >= 0) and (col < 5)

#This function checks if an index has a mine '#'.	
def isMine (row,col, arr) :
	if (arr[row][col] == "#"):
		return True
	else:
		return False

#This function checks the immediate adjacent points for mines and increament count accordingly.		
def adjacent_Count (row,col,grids) :
	count = 0
	if isValid(row-1,col) == True :
		if isMine(row-1,col,grids) == True:
			count += 1
			
	if isValid(row+1,col) == True:
		if isMine (row+1,col,grids) == True:
			count += 1
			
	if isValid(row,col+1) == True:
		if isMine(row,col+1,grids) == True :
			count += 1
		
	if isValid(row,col-1) == True:
		if isMine (row,col-1,grids) == True:
			count += 1
	
	if isValid(row-1,col+1) == True :
		if isMine(row-1,col+1,grids) == True:
			count += 1
		
	if isValid(row-1,col-1) == True:
		if isMine(row-1,col-1,grids) == True:
			count += 1
			
	if isValid(row+1,col+1) == True :
		if isMine(row+1,col+1,grids) == True:
			count += 1
	if isValid(row+1,col-1) == True :
		if isMine(row+1,col-1,grids) == True:
			count += 1
			
	return count

#This block of code calls the function 'mine()', and then it prints the mordified grid using a for loop.	
arr = mines(grid)	
for i in arr:	
	print (i)
