# Print out all the even numbers between 1 and 100

counter = 0

while counter <= 100:
    if counter % 2 == 0:
        print(counter, "Is an even number")
    else:
        print(counter, "is not even")
    counter = counter + 1