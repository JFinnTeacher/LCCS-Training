# Convert decimal number 43 to Binary equivalent

decimalNumber = 43

#create a list to build binaryNumber
binaryNumber = []

#my function to convert from decimal to binary
def decToBinary(decimalNumber):
    
    quotient = decimalNumber

    while quotient>1:
        quotient = quotient//2
        remainder = quotient%2
        
       # print(quotient, remainder)
        binaryNumber.append(remainder)
        
    #reverse list
    binaryNumber.reverse()

    return binaryNumber


#Display decimal number
print("Decimal Number: ",decimalNumber)

#Display expected result
# Base 2(binary)
bin_a = bin(decimalNumber)
print("Expected result:",bin_a)
#print(int(bin_a, 2)) #Base 2(binary)

#Call own custom function to convert decimal to binary
decToBinary(decimalNumber)

#Display final binary number
print("Binary Number: ",binaryNumber)

