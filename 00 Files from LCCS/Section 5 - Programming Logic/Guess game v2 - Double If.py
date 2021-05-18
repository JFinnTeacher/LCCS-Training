# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v2
# Purpose: A program to demonstrate the double if statement

import random

number = random.randint(1, 10)
# The next line can be commented out later ...
print(number) # have a sneak peek at the number to guess!

guess = int(input("Enter a number between 1 and 10: "))

# Evaluate the condition
if guess == number:
    print("Your guess was correct")
    print("Well done!")
    print(" ..... play again soon!")    
else:
    print("Hard luck!")
    print("Incorrect guess")
    print(" ..... play again soon!")    


print("Goodbye")

'''
# The code below is logically the same as the above ...

# Evaluate the condition
if guess != number:
    print("Hard luck!")
    print("Incorrect guess")
else:
    print("Your guess was correct")
    print("Well done!")

print(" ..... play again soon!")    
print("Goodbye")
'''
