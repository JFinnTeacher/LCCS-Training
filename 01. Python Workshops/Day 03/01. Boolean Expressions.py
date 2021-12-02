# print(True)
# print(False)
# print(type(True)) # Shows what type of item this is
# print(True+5) # Converts True to integer 1 for the sum
# print(int(True)) # Next two lines display the numerical value of the operator
# print(int(False))
# Relational Comparator - Compare 2 numbers
# <, <=, >, >=, ==, !=
# print(7<3) # Returns False
# print(7<=3) # Also returns False
# print(7>3) # Returns True
# print(7>=3) # Also returns True
# print(7==3) # Returns False
# print(7!=3) # Returns True
# print(7-4>=3) # Carries out the sum and then runs the expression

# Other operators - is, in
# print(5 is 5) # similar to equals
# print(5 is 6)
# print("r" in "rain") # will check the following string to see if the first value is in the second value and return true or false
# print("r" in "wet") # will return false
# print("ra" in "rain") # will check for any value
# myList = [1,2,3]
# print(2 in myList) # will go through the list looking for the vlaue and return true if found
# print(4 in myList) # Will return Flase

# Using Operators to compare strings
# print("Computer" == "Computer") # Operatorsd will also compare strings
# print("Computer" == "computer") # Does a direct comparison and is case sensetive
# print("Computer" != "computer") # the reverse (not) comparison will also work
# print("Computer" <= "Computer") # compares the Ascii Numbers to return a value and this is checked
# print(ord("c")) # returns ascii values of the letters
# print(ord("C"))

# Logical Operators - not, and, or (Uniary Operator - Only needs one value
# print(True) # The not Value will reverse the boolean output
# print(not True)
# print(False)
# print(not False)

#AND - True if only both are true
print(False and False)
print(False and True)
print(True and False)
print(True and True) # Will only return True if both are true all others false

#OR - True if any one is True
print(False or False)
print(False or True)
print(True or False)
print(True or True) # Will only return True if any one is True