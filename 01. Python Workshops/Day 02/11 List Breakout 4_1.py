#Breakout 4.1
import random

# Initialise the lists of words
article = ['the', 'a', 'one', 'some', 'any']
noun    = ['teacher', 'student', 'principal', 'library', 'school']
verb    =   ['taught', 'learned', 'read', 'walked', 'ran']
preposition =['to', 'from', 'over', 'under', 'on']

# Set the sentence wordList to be initially blank
wordList = []

# Choose a random article by using a random number as an index
# r = random.randint(0,4)
# word = article[r]
# wordList.append(word)
print("please enter 2 new articles")
article.append(input("What is your first word -->"))
article.append(input("What is your Second word -->"))


# Choose a random noun by using the choice command (method)
word = random.choice(article)
word = word.capitalize()
wordList.append(word)
word = random.choice(noun).capitalize()
wordList.append(word)
word = random.choice(verb).upper()
wordList.append(word)
word = random.choice(article)
wordList.append(word)
word = random.choice(noun).capitalize()
wordList.append(word)
word = random.choice(preposition)
wordList.append(word)
word = random.choice(verb).upper()
wordList.append(word)

# Display the sentence (so far)
print(wordList[0]+" "+wordList[1]+" "+wordList[2]+" "+wordList[3]+" "+wordList[4]+" "+wordList[5]+" "+wordList[6])

wordList = []
word = random.choice(article)
word = word.capitalize()
wordList.append(word)
word = random.choice(noun).capitalize()
wordList.append(word)
word = random.choice(verb).upper()
wordList.append(word)
word = random.choice(article)
wordList.append(word)
word = random.choice(noun).capitalize()
wordList.append(word)
word = random.choice(preposition)
wordList.append(word)
word = random.choice(verb).upper()
wordList.append(word)
print(wordList[0]+" "+wordList[1]+" "+wordList[2]+" "+wordList[3]+" "+wordList[4]+" "+wordList[5]+" "+wordList[6])

# Keep going! Get the next word ... keep going until you have a fully constructed sentence using the syntax rule given

#Extension exercise #1 - Capitalise the first word and any nouns in the sentence
#Extension exercise #2 - Change all the verbs to UPPER CASE
#Extension exercise #3 - When generating the random number (line 20), use the length of the relevant list as the second number (rather than having it hard-coded) 
#Extension exercise #4 - Ask the user to enter more articles/nouns/verbs/prepositions & add to the appropriate list
#Extension exercise #5 - Create a second sentence
#Extension exercise #6 - Make the nouns plural