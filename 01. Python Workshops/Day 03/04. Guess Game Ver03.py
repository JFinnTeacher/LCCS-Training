import random

number = random.randint(1, 10)
print(number)

guess = int(input("Enter a number between 1 and 10: "))

# Evaluate the condition, Python will start at the top and work down in sequence until if hits a
# block that runs. It will then exit the loop.
if guess == number: # Whatever comes after the if statement must be a boolean expression and will run if test is True
    print("Your guess was correct")
    print("Well done!")
elif guess < number: # Branches the code by allowing another if statement to run if answer is false above to see if number is too low
    print("Your guess was Too Low")
    print("Hard Luck")
else: # Will run if the result of all statements is false
    print("Your guess was Too High")
    print("Hard Luck")

print("Goodbye")