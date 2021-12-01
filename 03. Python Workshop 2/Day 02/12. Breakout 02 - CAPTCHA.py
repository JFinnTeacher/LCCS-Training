# Parsons Problem - Rearrange the blocks so that it works properly

#**************************************************************
def isValid():
    userEntry = input("Enter the CAPTCHA here >>>")
    return userEntry == captcha
#**************************************************************
captcha = ""
generateNewCAPTCHA()
displayCAPTCHA()
if isValid():
    print("Correct")
else:
    print("Incorrect")
#**************************************************************
def displayCAPTCHA():
    print("Prove that you are not a computer:")
    print("The CAPTCHA is shown here >>>", captcha)
#**************************************************************
import random
#**************************************************************
def generateNewCAPTCHA():
    global captcha
    #generate a random number between 65(A) and 90(Z)
    for i in range(random.randint(4,10)): #generate a CAPTCHA between 4 and 10 characters
        randomNo = random.randint(65,90)
        captcha = captcha + chr(randomNo)
#**************************************************************
