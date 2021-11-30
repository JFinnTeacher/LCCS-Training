from turtle import *

sides = int(input("How many sides does your shape have: "))
length = int(input("How long is each of the sides: "))

for shape in range(sides):
    forward(length)
    left(360/sides)