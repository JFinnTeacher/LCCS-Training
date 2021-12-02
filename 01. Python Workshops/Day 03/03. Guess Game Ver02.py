import random

number = random.randint(1, 10)
print(number)

guess = int(input("Enter a number between 1 and 10: "))

# Evaluate the condition
if guess == number: # Whatever comes after the if statement must be a boolean expression
    print("Your guess was correct")
    print("Well done!")
else:
    print("Your guess was incorrect")
    print("Hard Luck")
print("Goodbye")