# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Partial solution to breakout 4.1 - random sentence generator
# The full solution needs to be developed further ....

import random

# Initialise the lists of words
article = ['the', 'a', 'one', 'some', 'any']
noun    = ['teacher', 'student', 'principal', 'library', 'school']
verb    =   ['taught', 'learned', 'read', 'walked', 'ran']
preposition =['to', 'from', 'over', 'under', 'on']

#Add in more words
newArticle = input("Please enter another article ->")
article.append(newArticle)

newNoun = input("Please enter another noun ->")
noun.append(newNoun)

newVerb = input("Please enter another verb ->")
verb.append(newVerb)

newPreposition = input("Please enter another preposition ->")
preposition.append(newPreposition)

# Set the sentence wordList to be initially blank
wordList = []
wordList2 =[]

# Choose a random article by using a random number as an index
#First words--------------------------------------
listLength = len(article)
print(listLength)
r = random.randint(0,listLength - 1)
word = article[r]
word = word.capitalize()
wordList.append(word)

r = random.randint(0,listLength - 1)
word = article[r]
word = word.capitalize()
wordList2.append(word)
#-------------------------------------------------------

#Second words
# Choose a random noun by using the choice command (method)
word = random.choice(noun)
word = word + "s"
word = word.capitalize()
wordList.append(word)

word = random.choice(noun)
word = word + "s"
word = word.capitalize()
wordList2.append(word)
#------------------------------------------------------------

#Third words
word = random.choice(verb)
word = word.upper()
wordList.append(word)

word = random.choice(verb)
word = word.upper()
wordList2.append(word)
#----------------------------------------------------------------

#Forth Words

word = random.choice(article)
wordList.append(word)

word = random.choice(article)
wordList2.append(word)
#----------------------------------------------------------------------

#Fifth word
word = random.choice(noun)
word = word + "s"
word = word.capitalize()
wordList.append(word)

word = random.choice(noun)
word = word + "s"
word = word.capitalize()
wordList2.append(word)
#--------------------------------------------------------------------

#Sixth word
word = random.choice(preposition)
wordList.append(word)

word = random.choice(preposition)
wordList2.append(word)
#-----------------------------------------------------------------------

#Seventh Word
word = random.choice(verb)
word = word.upper()
wordList.append(word)

word = random.choice(verb)
word = word.upper()
wordList2.append(word)
#--------------------------------------------------------------------------

# Display the sentence (so far)
print(wordList[0]+" "+wordList[1]+" "+wordList[2]+" "+wordList[3]+" "+wordList[4]+" "+wordList[5]+" "+wordList[6])

print(wordList2[0]+" "+wordList2[1]+" "+wordList2[2]+" "+wordList2[3]+" "+wordList2[4]+" "+wordList2[5]+" "+wordList2[6])



# Keep going! Get the next word ... keep going until you have a fully constructed sentence using the syntax rule given

#Extension exercise #1 - Capitalise the first word and any nouns in the sentence
#Extension exercise #2 - Change all the verbs to UPPER CASE
#Extension exercise #3 - When generating the random number (line 20), use the length of the relevant list as the second number (rather than having it hard-coded) 
#Extension exercise #4 - Ask the user to enter more articles/nouns/verbs/prepositions & add to the appropriate list
#Extension exercise #5 - Create a second sentence
#Extension exercise #6 - Make the nouns plural

