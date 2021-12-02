import random

number = random.randint(1, 10)
print(number)
counter = 0

while counter < 3:
    guess = int(input("Enter a number between 1 and 10: "))

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