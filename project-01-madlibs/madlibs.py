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



#parts of speech lists
adj_list = ['stinky' , 'ugly', 'wild', 'moldy', 'violent', 'evil', 'sick', 'filthy'] 

verb_list = ['choke', 'fart', 'kick', 'melt', 'fight', 'snore', 'explode', 'laugh']

noun_list = ['toes', 'waste','dog','cat','toilet','butt','cockroach','failure']

hero_list = ['Kenzie', 'Chelsea', 'Jasmine']



#create function to locate and change adjectives
def change_adjective():
    for i in range(len(content_words)): #getting length of the content words(the text file) and setting it to the range of the for loop.
      if content_words[i] == '<ADJECTIVE>':#content_words[i] means the element at index 'i' of list. Finds location where string word in split file = <ADJECTIVE>
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




change_verb() #calling all the functions in the end 
change_noun() # calling all functions at the end will make it print whatever is returned --> " ".join(content_words)
change_adjective()




#factoring in capitalization
MLstory = " ".join(content_words) # Removes the list aspect and creates spaces between 

#Helped by Julianne Agular(lines 57-58)
MLstory = MLstory.split('. ') #splits story into list after every period
MLstory = [w.capitalize() for w in MLstory] #capitalizes the start of every element in list(the split)



MLstory = ". ".join(MLstory)
MLstory = MLstory.split(' ')#split by spaces so that I can do replacement with def change_hero function.

#create function to randomize hero name and store it to be repeated
def change_hero(n): 
  hero = random.choice(hero_list) #the randomized name will be stored. 
  for i in range(len(MLstory)):
    if MLstory[i] == '<hero>':
      MLstory[i] = MLstory[i].replace('<hero>',hero)#the name will be randomized and stored in variable 'hero' and all other occurences will also be the name in 'hero'
    elif MLstory[i] == '<hero>.':
      MLstory[i] = MLstory[i].replace('<hero>.',hero)
  return " ".join(MLstory)

print(change_hero(hero_list))

