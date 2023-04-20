Irish={'GRMA':"Go Raibh Maith Agat","OMD":"O Mo Dhia","GOA":"Gaire Os Ard","MGL":"Maith Go Leor"}


acronyms={'Irish':{'GRMA':"Go Raibh Maith Agat","OMD":"O Mo Dhia","GOA":"Gaire Os Ard","MGL":"Maith Go Leor"},
          'English': {'OMG': "Oh My God!",'LOL':'Laugh out Loud','IMHO':'In My Humble Opinion'},
          'German': {'USW':'Und So Weiter', 'ZB':'Zum Beispel'}}

# lets look at the dictionary Irish
# two main ways of iterating through the elements in the dictionary
# one gets the keys

for item in Irish:
    print(item)


#the other gets the values
for item in Irish:
    print(Irish[item])


#this gets the keys
for item in acronyms:
    print(item)


#your students may do one of the following when iterating over nested dictionaries

# Let's try to find all the acronyms in our dictionary - we will iterate first over the irish english german dictionaries
# inside this we will iterate through the elements
# try this
for item in acronyms:
    for thing in item:
        print(thing)


# we wanted the acronyms. we didn't get it. the thing loop iterates over the string item!

for item in acronyms:
    print(acronyms[item])
    

# we wanted the acronyms, instead we got the dictionaries. this isn't what we want
# but we are on the right path - we now know how to access the dictionaries
# with this strategy we can access each element in the new dictionaries quite easily

for item in acronyms:
    for thing in acronyms[item]:
        print(thing)
        print(acronyms[item][thing])# I added this to get 
        
# this worked, great!
# we have to do one iteration over the keys in acronyms and then
# do a second interation over the keys in each entry in acronyms
# which is why the acronyms[item] is needed




#we can also do this with list comprehensions, below:    
irishKeys = [item for item in Irish]
irishValues = [Irish[item] for item in Irish]
print(irishKeys)
print(irishValues)
