# myString = "abc"
# result = myString.isdigit() # This function is checking to see if the string is all digits
# print(result)

# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate Boolean functions

# A function to determine evenness
def isEven(number):
    if (number % 2 == 0): #checks to see if there is no remainder then this is even
        return True # if even returns true
    else:
        return False # if not even returns false

def isOdd(number):
    if (number % 2 != 0): #checks to see if there is no remainder then this is even
        return True # if even returns true
    else:
        return False # if not even returns false

# display even numbers < 100
for i in range (100):
    if isEven(i): # if this value is true then will run the next line.
        print(i)
        
for i in range (100):
    if isOdd(i):
        print(i)

'''
# A function to determine oddness
def isOdd(number):
    return not isEven(number)

for i in range (100):
    if isOdd(i):
        print(i)
'''