#countdown using recursion
def countDown(n):
    if n<=0:
        print("End")
    else:
        print(n);
        countDown(n-1)

#countup using recursion
def countUp(n):
    if n<=0:
        print("Start")
    else:
        countUp(n-1)
        print(n);

countDown(5)
print("==========")
countUp(5)

#countup/down using iteration 
def countDownWhile(n):
    while n > 0:
        print(n)
        n=n-1
    print("End")
    
def countDownFor(n):
    for counter in range(n, 0, -1):
        print(counter)
    print("End")

def countUpWhile(n):
    counter = 1
    while counter <= n:
        print(counter)
        counter=counter+1
    print("End")
    
def countUpFor(n):
    for counter in range(1, n+1):
        print(counter)
    print("End")
    
print("==========")   
countDownWhile(5)
print("==========")
countDownFor(5)
print("==========")
countUpWhile(5)
print("==========")
countUpFor(5)
    

def factorial(n):
    print(n)
    if n == 1:   
       return n   
    else:       
       return n * factorial(n-1)
ans = factorial(5)
print(ans) 


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(">", fibonacci(4))




#Fibonacci without recursion
nterms = 50
num = 0
before1 = 0
before2 = 1
while nterms > 0:
    num = before1 + before2
    print(num)
    #circle(num,extent)
    before1 = before2
    before2 = num
    nterms=nterms - 1