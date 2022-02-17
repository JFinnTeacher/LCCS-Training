# A program to find the median of a list of values
# Version 1

# Initialise a list of values
L = ["jim","Pat", "John", "Rob", "Sue"]

# To find the median we need to sort the list
L.sort() # the values are sorted 'in place'

# The next step is to find the index of the middle value
num_values = len(L)
mid = num_values//2 # floor division will round down

median = L[mid] # the median is in the middle

# Display the result
print("The median value is: %.2f" %median)
