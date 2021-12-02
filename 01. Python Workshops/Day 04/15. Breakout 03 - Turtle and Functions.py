from turtle import *

def drawSquare(sides): 
#     forward(sides) # Standard Method
#     right(90)
#     forward(sides)
#     right(90)
#     forward(sides)
#     right(90)
#     forward(sides)
#     right(90)
    for side in range(4): # Using Iteration
        forward(sides)
        left(90)
    
def drawRect(side01,side02): 
#     forward(side01) # Standard Method for rectangle
#     right(90)
#     forward(side02)
#     right(90)
#     forward(side01)
#     right(90)
#     forward(side02)
#     right(90)
    for side in range(2): # Using Iteration
        forward(side01)
        right(90)
        forward(side02)
        right(90)
    

drawSquare(100)
drawRect(100,50)