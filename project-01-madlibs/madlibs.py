"""These are the extras I completed:
1. Imported the file from another text file
2.
3.

"""

import random 

#open, read, and write file
f = open("madlibs.txt", "r") # madlibs.txt = locaton of the file. Opens file and stores in f. "r" opens in read mode.
content = f.read() 
content_words = content.split() #seperates charcters with white spaces between them

adj_list = ['stinky' , 'ugly', 'wild', 'moldy', 'violent', 'angry', 'sick', 'filthy'] #adjective list

verb_list = ['stab', 'fear', 'kick', 'melt', 'fight', 'harass', 'explode', 'hit']

noun_list = ['toes', 'idiot', 'dog','cat','bathroom','butt','cockroach','failure']

hero_list = ['Kenzie', 'Chelsea', 'Jasmine']

#create function to locate and change adjectives
def change_adjective():
    for i in range(len(content_words)): #getting length of the content words(the text file) and setting it to the range of the for loop.
      if content_words[i] == '<ADJECTIVE>':# content_words[i] means the element at index 'i' of list. Finds location where string word in split file = <ADJECTIVE>
        content_words[i] = random.choice(adj_list) #replaces the index position when the statement above is True with random element from adj_list. 
    return " ".join(content_words)

#create function to locate and change nouns. Same concept as the change_adjective function above
def change_noun():
    for i in range(len(content_words)):
      if content_words[i] == '<NOUN>':
        content_words[i] = random.choice(noun_list)
    return " ".join(content_words)

#create function to locate and change verbs. Same concept
def change_verb():
    for i in range(len(content_words)):
      if content_words[i] == '<VERB>':
        content_words[i] = random.choice(verb_list)
    return " ".join(content_words)

def change_hero():
    for i in range(len(content_words)):
      if content_words[i] == '<HERO>':
        content_words[i] = random.choice(hero_list)
    return " ".join(content_words)


change_verb() #calling all the functions in the end 
change_noun() # calling all functions at the end will make it print whatever is returned
change_adjective()
change_hero()

print(" ".join(content_words))# It will not print original paragraph but the modified ones. Removes the list aspect and creates spaces between 
"........."

print("based on a true story.")