def calcArea(length,width): # Define the function
    area = length * width # Carry out the calculation
    # print("The area of the shape is: ", area) # Print the result to the screen
    return area # Returns the value to the main program
    
length = int(input("What is the length of the figure: ")) # Collect the 2 arguments
width = int(input("What is the width of the figure: "))
# result = calcArea(length,width) # Pass the arguments to the function and collect the return value to variable
# print("The area of the shape is: ", result) # print the result from the variable

print("The area of the shape is: ", calcArea(length,width)) # Inline processing is calling the function directly