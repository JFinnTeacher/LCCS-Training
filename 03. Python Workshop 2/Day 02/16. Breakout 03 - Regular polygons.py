from turtle import *
import random

def setTurtle (size,penColor):
    hideturtle()
    color(penColor)
    pensize(size)
    
def drawPolygon(sides,length):
    for side in range(sides):
        forward(length)
        left(360/sides)

def numberPoly(number):
    for items in range(number):
        penup()
        setpos(random.randint(-200,200),random.randint(-200,200))
        pendown()
        drawPolygon(polySide,polyLength)
        
penColor = input("What colour would you like red,green,blue: ")
size = int(input("What thickness 1 - 10 should the pen be: "))
polySide = int(input("How many sides does your polygon contain: "))
polyLength = int(input("How long is each side of the polygon: "))
numPoly = int(input("How many polygons would you like to draw randomly: "))
setTurtle(size,penColor)
numberPoly(numPoly)
# drawPolygon(polySide,polyLength)
exitonclick()