# string1 = "Hello World"
# string2 = 42
# string3 = "42"
# # prints the string
# print(string1)
# print(string2)
# print(string3)
# #displays the type of data stored in the variable
# print(type(string1))
# print(type(string2))
# print(type(string3))

# Adding Strings together Python can manipulate strings to modify them
# x="42"
# y="56"
# 
# z= x + y
# 
# print(z)
# print(type(z))
# # Strings can be add multiplied etc in Python only works for multiply
# print(x * 3)

# Display ascii code using python - ord function will return the ascii code of a letter
# x="A"
# 
# print(ord(x)+1)
# # chr function will take the number and return the corresponding ascii character
# print(chr(125))

# String Indexing
# 
# x="Hello"
# # Square brackets will allow you to display a specific letter = Indexing starts from 0
# print(x[0])
# # Displays the ascii code of the letter in the string above
# print(ord(x[0]))

string1 = "Hello"
string1.replace("H","B") # nothing happens as the string is immutable and cannot change. this needs to be passed to a new string
string2 = string1.replace("H","B") 
print(string1) #  This string is immutable
print(string2) 
