import random # imports the random library/funtion random
# import turtle # imports the turtle library
from turtle import forward # Tells python to import forward to the current library

randomNumber = random.randint(1,10) # from the random library run randint
# turtle.forward(100) # from the turtle library use the forward function
forward(100) # No longer need to add turlte library as it is now natively defined.
print(randomNumber)