#LCCS
#April 2023
#Analysis of Binary Search algorithm p77

import random
def binary_search(v, L):
    global comparisons
    low = 0
    high = len(L)-1
    while (low <= high):
        index = (low+high)//2
        comparisons = comparisons + 1

        if L[index] == v:
            return index
        elif L[index] < v:
            low = index + 1
        else:
            high = index - 1
    return -1

# Driver code (test harness)...
print("%s\t\t %s\t\t %s" %("List Size (N)", "Found Index", "#Comparisons"))

for list_size in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    some_list = list(range(list_size))
    comparisons = 0
#    target = -1 # worst case because -1 never exists
    target = random.randrange(len(some_list)) #average case
    pos = binary_search(target, some_list)
    print("%d\t\t %d\t\t %d" %(len(some_list), pos, comparisons))