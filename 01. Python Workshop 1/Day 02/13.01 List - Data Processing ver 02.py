# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate the average height of 5 people

# A program to calculate the average height of 5 people
# The heights are stored in a file called 'heights.txt'

from statistics import *

heightFile = open("heights.txt","r") # Open the file

totalHeight = [] # Initialise a running total to zero
height = float(heightFile.readline())   # read the first value
totalHeight.append(height) # keep a running total
height = float(heightFile.readline())   # read the first value
totalHeight.append(height) # keep a running total
height = float(heightFile.readline())   # read the first value
totalHeight.append(height) # keep a running total
# height = float(heightFile.readline())   # read the first value
totalHeight.append(float(heightFile.readline())) # keep a running total
#height = float(heightFile.readline())   # read the first value
totalHeight.append(float(heightFile.readline())) # keep a running total


# Display the result
print(totalHeight)
print(mean(totalHeight))
print(median(totalHeight))

# Close the file
heightFile.close()