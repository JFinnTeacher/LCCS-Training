#LCCS
#April 2023
#Linear Search algorithm

def linear_search(v, L):      #function with 2 parameters, L is list, v is what we're searching for
    for i in range(len(L)):   #iterates through the list L
        if L[i] == v:
            return i          #returns the position of the what we're looking for!
        
    return -1    #not found

#Driver code...
keys = [15, 4, 41, 13, 24, 14, 12, 21, 22]
argument = int(input("Enter a target value:"))

result = linear_search(argument, keys)

if (result != -1):
    print("%d found at position %d" %(argument, result))
else:
    print("%d not found. Return value is %d" %(argument, result))