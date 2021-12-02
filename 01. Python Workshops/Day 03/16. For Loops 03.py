from turtle import *

for triangle in range(3):
    forward(100)
    left(120)
    
penup() # Turtle command to lift the pencil
backward(200) # Moving to a new location
pendown() # Lower the pencil to draw the next shape

for rectangle in range(2):
    forward(100)
    left(90)
    forward(50)
    left(90)
    
penup()
forward(400)
pendown()

for hexagon in range(6):
    forward(100)
    left(60)