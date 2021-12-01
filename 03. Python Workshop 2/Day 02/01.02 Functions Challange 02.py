def homework(name): # adding an argument allows you to pass information into the function
    print(name, "loves to do his homework")
    print("He never misses a day")
    print("He even loves the men in white")
    print("Who are taking him away")
    
homework("David")
print("The end")

def homework(name):
    print(name, "loves to do his homework")
    print("He never misses a day")
    print("He even loves the men in white")
    print("Who are taking him away")
    
person = input("What is your name: ") # You can collect a parameter from an input to pass it in
homework(person)
print("The end")

def homework(name,pronoun): # can collect multiple arguments
    print(name, "loves to do",pronoun, "homework")
    print("He never misses a day")
    print("He even loves the men in white")
    print("Who are taking him away")
    
person = input("What is your name: ") # You can collect a parameter from an input to pass it in
title = input("What pronoun do you use (his/her): ") # collects pronoun
homework(person,title) # The order collected here must match the order in the definition name,pronoun
print("The end")