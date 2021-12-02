def calcArea(length,width): # Define the function
    area = length * width # Carry out the calculation
    print("The area of the shape is: ", area) # Print the result to the screen
    
length = int(input("What is the length of the figure: ")) # Collect the 2 arguments
width = int(input("What is the width of the figure: "))
calcArea(length,width) # Pass the arguments to the function

def calcVolume(length,width,depth): # Define the function
    area = length * width * depth # Carry out the calculation
    print("The volume of the shape is: ", area) # Print the result to the screen
    
length = int(input("What is the length of the figure: ")) # Collect the 3 arguments
width = int(input("What is the width of the figure: "))
depth = int(input("What is the depth of the figure: "))
calcVolume(length,width,depth) # Pass the arguments to the function