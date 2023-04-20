#to recap on indexing strings and lists

stringOne = 'This is a string with lots of characters.'
#            01234567890123456789012345678901234567890            
print(stringOne)

#Accessing single characters from a string
firstCharacter = stringOne[0]
fifteenthCharacter = stringOne[14]
lastCharacter = stringOne[-1]
print(firstCharacter)
print(fifteenthCharacter)
print(lastCharacter)


#Accessing a segment of a string
stringSlice = stringOne[8:21]
print(stringSlice)


#Defining a list
listOne = ['lean','tilt','bank','tip','pitch','nod','dip']


#Lists are accessed in a similar way to strings
secondElement = listOne[1]
insidelist = listOne[2:6]
print(secondElement)
print(insidelist)

#Dictionaries are created differently, requiring a key:value pair for each element.
#Here the keys are the acronyms and the values are what they stand for
Gaeilge={'GRMA':"Go Raibh Maith Agat","OMD":"O Mo Dhia","GOA":"Gaire Os Ard","MGL":"Maith Go Leor"}

#you can get values by calling dict[key]
thankYou = Gaeilge['GRMA']
print(thankYou)
print(Gaeilge['GRMA'])

#the list of keys can be found using the keys() method on the dictionary
keys = Gaeilge.keys()
print(keys)

#accessing dictionary values by their keys
omg1 = Gaeilge['OMD']
omg2 = Gaeilge.get('OMD')

print(omg1)
print(omg2)

#let's build in a mistake. if the key cannot be found the program will terminate
#omg1 = Gaeilge['GAO']

#'GAO' is not one of the keys in Gaeilge. The get method looks for 'GAO' and if it cannot find it returns 'acronym missing')
omg2 = Gaeilge.get('GAO','acronym missing')

#print(omg1)
print(omg2)


#removing an item using .pop(key)
print(Gaeilge)
Gaeilge.pop('OMD')
print(Gaeilge)


#updating dictionary elements using bracket or .update(key:value) notation
Gaeilge['GOA']='Gaire Oos Ard'
print(Gaeilge)
Gaeilge.update({'GOA':'Gallimh Os Ard'})
print(Gaeilge)

#deleting all elements of a dictionary
Gaeilge.clear()
print(Gaeilge)