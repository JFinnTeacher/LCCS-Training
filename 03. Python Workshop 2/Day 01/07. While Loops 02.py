# show all squared numbers
# 
# x = 1
#     
# while x <= 1000:
#     print("The Square of", x , "is", x*x)
#     x = x+1
    
# Protect against invalid results using while loop
result = int(input("Enter the result: "))

# This is impoosible to be true as no number can be in this range while result <0 and result >100

while result <0 or result > 100:
    print("Invalid result")
    result = int(input("Enter the result: "))

print("Result Entered")
