"""These are the extras I completed:
1. Imported and read the file from another text file
2. Dealt with capitalization at the beginning of the sentence
3. Select a replacement randomly but then keep reusing that replacement.
"""
import random 

#open, read, and write file
f = open("madlibs.txt", "r") # madlibs.txt = locaton of the file. Opens file and stores in f. "r" opens in read mode.
content = f.read() 
content_words = content.split() #seperates charcters with white spaces between them

adj_list = ['stinky' , 'ugly', 'wild', 'moldy', 'violent', 'evil', 'sick', 'filthy'] #adjective list

verb_list = ['stab', '', 'kick', 'melt', 'fight', 'snore', 'explode', 'laugh']

noun_list = ['toes', 'waste', 'dog','cat','bathroom','butt','cockroach','failure']

hero_list = ['Chelsea', 'Jasmine']

#create function to locate and change adjectives
def change_adjective():
    for i in range(len(content_words)): #getting length of the content words(the text file) and setting it to the range of the for loop.
      if content_words[i] == '<ADJECTIVE>':# content_words[i] means the element at index 'i' of list. Finds location where string word in split file = <ADJECTIVE>
        content_words[i] = random.choice(adj_list) #replaces the index position when the statement above is True with random element from adj_list.
      elif content_words[i] == '<ADJECTIVE>.':
        content_words[i] = random.choice(adj_list) + "."
    return " ".join(content_words)

#create function to locate and change nouns. Same concept as the change_adjective function above
def change_noun():
    for i in range(len(content_words)):
      if content_words[i] == '<NOUN>':
        content_words[i] = random.choice(noun_list)
      elif content_words[i] == '<NOUN>.':
        content_words[i] = random.choice(noun_list) + "." #adds a period at the end of the part of speech if there is one in the original text file.
    return " ".join(content_words)

#create function to locate and change verbs. Same concept
def change_verb():
    for i in range(len(content_words)):
      if content_words[i] == '<VERB>':
        content_words[i] = random.choice(verb_list)
      elif content_words[i] == '<VERB>.':
        content_words[i] = random.choice(verb_list) + "."
    return " ".join(content_words)

#create function to locate and change the hero name.
def change_hero():
    for i in range(len(content_words)):
      if content_words[i] == '<HERO>':
        content_words[i] = random.choice(hero_list)
      elif content_words[i] == '<HERO>.':
        content_words[i] = random.choice(hero_list) + "."
    return " ".join(content_words)

change_verb() #calling all the functions in the end 
change_noun() # calling all functions at the end will make it print whatever is returned --> " ".join(content_words)
change_adjective()
change_hero()

#factoring in capitalization

MLstory = " ".join(content_words) # Removes the list aspect and creates spaces between 
sentences = MLstory.split('. ') # splits story into sentences
for i in range(len(sentences)):
  words = sentences[i].split(' ')
  words[0] = words[0].capitalize()# capitalize first word

print(sentences)
