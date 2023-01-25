# Simple (Selection) Sort v1 from Algorithims notebook
 
# 1. Initialise an unsorted list 
L = [9, 6, 10, 4, 8, 5, 7] 
# 2. Initialise a marker 
marker = 0  
 
# 3. Traverse through all list items 
while marker < len(L): 
    # 4. Find the minimum item to the right of the marker 
    index_of_min = marker 
    for j in range(marker+1, len(L)):  
        if L[index_of_min] > L[j]:  
            index_of_min = j 
 
    # 5. Exchange the smallest item with the item at the marker 
    temp = L[marker] # save the item at the marker 
    L[marker] = L[index_of_min] # copy 1 
    L[index_of_min] = temp # copy 2 
     
    # 6. Advance the marker to the right by 1 position 
    marker = marker+1 
 
# 7. Stop 