#LCCS
#April 2023
#Binary search algorithm 

def binary_search(v, L):
 
    low = 0
    high = len(L)-1
 
    while (low <= high):
        mid = (low+high)//2
        
        if L[mid] == v:
            return mid
        elif L[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1 

# Driver code ...
keys = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
argument = int(input("Enter a target value: "))
 
result = binary_search(argument, keys)

if (result != -1):
    print("%d found at position %d" %(argument, result))
else:
    print("%d not found. Return value is %d" %(argument, result))