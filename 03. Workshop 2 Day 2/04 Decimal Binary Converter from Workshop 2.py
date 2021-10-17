# Convert the decimal number 19 into binary
print('enter a number')
number = input()
quotient = int(number)
array = []
while quotient != 0:
    new_quotient = quotient // 2 # floor division : how many 2s in 19
    remainder = quotient % 2  # modulus : remainder
    array.append(remainder)
    print(new_quotient, remainder)
    quotient = new_quotient
array.reverse()
print(array)
#Convert binary to decimal
print('enter a number')
number2 = input()
binary = int(number2)
decimalTotal = 0
counter = 0
total = 0
while binary !=0:
    newBinary = binary // 10
    binaryRemainder = binary % 10
    print(newBinary, binaryRemainder)
    total = binaryRemainder * ( 2**counter)
    decimalTotal = decimalTotal + total
    counter+=1
    binary = newBinary
print(decimalTotal)