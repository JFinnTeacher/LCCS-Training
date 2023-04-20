#LCCS
#April 2023
#Analysis of Linear Search algorithm p75

import random

def linear_search(v, L):
    global comparisons
    
    for index in range(len(L)):
        comparisons = comparisons + 1
        if L[index] == v:
            return index

    return -1 # not found

# Driver code ...
print("%s\t\t %s\t\t %s" %("List Size", "Found Index", "#Comparisons"))

for list_size in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    some_list = list(range(list_size))
#    print(some_list)
    random.shuffle(some_list) # randomise the list
#    print(some_list)
    comparisons = 0
    target = -1 # worst case because -1 never exists
#    target = random.randrange(len(some_list)) #average case
    pos = linear_search(target, some_list)
    print("%d\t\t %d\t\t %d" %(len(some_list), pos, comparisons))