# come back and fix

def isEqual(num1,num2):
    if num1 == num2:
        return True
    else:
        return False
    
num1 = input(int("What is your first number: "))
num2= input(int("What is your second number: "))

areSame = isEqual(num1,num2)
if areSame == True:
    print(num1, " is equal to ",num2)
else:
    print(num1, "is not equal to ", num2)