# Recursion keeps opening new stacks and leaves them open until the loop has finished then
# it will finalise each stack pass on the output and close the stack.

#Countdown using recursion
def countDown(n):
    if n<=0:
        print("End")
    else:
        print(n)
        countDown(n-1) # This will run until 0 is reached before moving on so it prints first
# Countup using recursion        
def countUp(n):
    if n<=0:
        print("Start")
    else:
        countUp(n-1) # Here it will run before printing and prints the numbers in reverse order.
        print(n)
        
countDown(5)
print("===============")
countUp(5)
'''
Once the recurson line is reached the code will remain on that line generating new stacks before
it will move on to the next line. The order of recursion is very important.
It is also important to have a stop point as otherwise it will continue until it crashes
'''