import random 

#create list of words to randomly generate into madlibs. Assign list to variables

ADJECTIVES = ['stinky' , 'ugly', 'wild', 'moldy', 'violent', 'angry', 'sick', 'filthy']

VERBS = ['stab', 'fear', 'cook', 'swat', 'fight', 'harass', 'explode', 'hit']

NOUNS = ['toes', 'idiot', 'dog','cat','bathroom','butt','cockroach','poo']

HEROS = ['Kenzie', 'Chelsea', 'Jasmine']

f = open("madlibs.txt", "r")
content = f.read()
content_words = content.split()

#create function to identify and replace 
def change_adjective():
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  if content_words == '<ADJECTIVE>':
      for words in ADJECTIVES:
        result = content_words.replace('<ADJECTIVES', random.choice(ADJECTIVES))
    return result

    print(result)

