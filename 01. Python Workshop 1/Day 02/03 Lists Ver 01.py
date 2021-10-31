#Big difference between lists and strings is lists are mutable and strings are not.

boysNames = ['John', "Jim", "Alex", "Fred"]
girlsNames = ["Sarah", "Alex", "Pat", "Mary"]
favouriteSongs = ["Moondance", "Linger", "Stairway"]
fruits = ["Strawberry", "Lemon", "Orange", "Raspberry", "Cherry"]
vehicleCount = [0,0,0,0,0,0]
accountDetails = [1234, "xyz", "Alex", "1 main St", 827.56]

#Test print of lists

# print(boysNames)
# print(accountDetails)

# Common List Operations

# #This adds the 2 lists together in the order of the concatation. the result is still a list
# names = boysNames + girlsNames
# print(names)
# # Not preferred solution as the boysNames list has changed and loses its meaning. Method above is preferred option
# boysNames = boysNames + girlsNames
# print(boysNames)

#Indexing of lists unlike string index prints the list entry.

# print(boysNames[3])

#Modifying Lists

print(boysNames)
boysNames[1] = "James" # This replaces the item at postion 2 with the new entry
print(boysNames)

      