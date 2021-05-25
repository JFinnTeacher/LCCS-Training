#Big difference between lists and strings is lists are mutable and strings are not.

boysNames = ['John', "Jim", "Alex", "Fred"]
girlsNames = ["Sarah", "Alex", "Pat", "Mary"]
favouriteSongs = ["Moondance", "Linger", "Stairway"]
fruits = ["Strawberry", "Lemon", "Orange", "Raspberry", "Cherry"]
vehicleCount = [0,0,0,0,0,0]
accountDetails = [1234, "xyz", "Alex", "1 main St", 827.56]

# Making Changes to list
# Commands below are making modifications to the list by replacing list enteries with other items and moving items
# around by swapping them

print(fruits)
fruits[0] = "Apple"
fruit = "Melon"
fruits[1] = fruit
fruits[2] = "Raspberry"
fruits[3] = fruits[4]
fruits[4] = "Pineapple"

print(fruits)