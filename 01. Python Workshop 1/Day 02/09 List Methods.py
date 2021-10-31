# List methods from 109 in Handbook

fruits = ['Strawberry', 'Lemon', 'Orange', 'Raspberry', 'Cherry']
vegs = ["Potato", "Turnip", "Carrot"]

print(fruits)
fruits.extend(vegs)
print(fruits)
print("Number of items", fruits.count("Lemon"))
print("The index value for Turnip is", fruits.index("Turnip"))
fruits.insert(5,"Parsnip")
print(fruits)
value = fruits.pop()
print("Value", value, "List", fruits)