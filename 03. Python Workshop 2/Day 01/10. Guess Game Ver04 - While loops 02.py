# Modify the random number
# Get input on number of guesses

import random
limit = int(input("What number would you like to guess up to: "))
number = random.randint(1, limit)
print(number)

counter = 0
tries = int(input("How many goes would you like: "))

while counter < tries:
    guess = int(input("Enter a number between 1 and "+ str(limit))) # has to concantate and add limit as a string to this

    if guess == number: 
        print("Your guess was correct")
        print("Well done!")
        break # This command ends the while loop immediately
    elif guess < number: 
        print("Your guess was Too Low")
        print("Hard Luck")
    else: 
        print("Your guess was Too High")
        print("Hard Luck")
    counter = counter + 1

print("Goodbye")