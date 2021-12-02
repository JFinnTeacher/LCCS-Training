mark = int(input("Enter your Percentage: "))
print(mark)

if mark >= 90:
    print("Your grade is H1")
elif mark >= 80:
    print("Your grade is H2")
elif mark >= 70:
    print("Your grade is H3")
elif mark >= 60:
    print("Your grade is H4")
elif mark >= 50:
    print("Your grade is H5")
elif mark >= 40:
    print("Your grade is H6")
elif mark >= 30:
    print("Your grade is H7")
elif mark <= 29 and mark >= 0:
    print("Your grade is H8")
else:
    print("Invalid Number")