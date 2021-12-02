# Convert Decimal number 43 to binary

# quotient = 19//2 # How many 2s are in 19
# remainder = 19 % 2 # modulus: remainder
# print(quotient, remainder)
# 
# quotient = 9//2 # How many 2s are in 9
# remainder = 9 % 2 # modulus: remainder
# print(quotient, remainder)
# 
# quotient = 4//2 # How many 2s are in 4
# remainder = 4 % 2 # modulus: remainder
# print(quotient, remainder)
# 
# quotient = 2//2 # How many 2s are in 2
# remainder = 2 % 2 # modulus: remainder
# print(quotient, remainder)
# 
# quotient = 1//2 # How many 2s are in 1
# remainder = 1 % 2 # modulus: remainder
# print(quotient, remainder)

quotient = 43
binary = []
while quotient > 0:
    remainder = quotient % 2
    quotient = quotient // 2
    binary.append(remainder)
binary.reverse()
binstr = ""
for elem in binary:
    binstr = binstr + str(elem)
print("Binary Number", binstr)