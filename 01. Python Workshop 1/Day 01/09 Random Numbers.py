#find Average of 5 random numbers
#Page 47 of Notes

import random

low = random.randint(1,100)
high = random.randint(low,100)

#Generate the 5 random numbers
n1 = random.randint(low, high)
n2 = random.randint(low, high)
n3 = random.randint(low, high)
n4 = random.randint(low, high)
n5 = random.randint(low, high)

#find average
average = (n1+n2+n3+n4+n5) /5

# Display the 5 numbers and answer
print("The average of",n1,n2,n3,n4,n5,"is",average)