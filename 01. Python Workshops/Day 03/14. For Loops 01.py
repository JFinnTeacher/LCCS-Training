# Simple for loop
# The variable counter is local to that for loop only and does not exist outside of the for loop

for counter in range(10): # Will iterate through a list of numbers 0 to 9
    print("Hello World", counter)

print("Goodbye")

for counter in range(1,20): # will iterate through a list from 1 to 19
    print("Hello World", counter)

print("Goodbye")

for counter in range(1,20,2):# will iterate through a list from 1 to 19 in steps of 2
    print("Hello World", counter)

print("Goodbye")

from turtle import *

for count in range(4):
    forward(100)
    left(90)

for count in range(3):
    back(100)
    left(120)