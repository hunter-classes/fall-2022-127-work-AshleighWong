import random 
f = open("madlibs.txt", "r") 
content = f.read() 
content_words = content.split()

adj_list = ['stinky' , 'ugly', 'wild', 'moldy', 'violent', 'angry', 'sick', 'filthy']

verb_list = ['stab', 'fear', 'cook', 'swat', 'fight', 'harass', 'explode', 'hit']

noun_list = ['toes', 'idiot', 'dog','cat','bathroom','butt','cockroach','poo']

heros_list = ['Kenzie', 'Chelsea', 'Jasmine']

def change_adjective():
    for i in range(len(content_words)):
      if content_words[i] == '<ADJECTIVE>'
        content_words[i] = random.choice(adj_list) 
    return " ".join(content_words)

def change_noun():
    for i in range(len(content_words)):
      if content_words[i] == '<NOUN>':
        content_words[i] = random.choice(noun_list)
    return " ".join(content_words)

def change_verb():
    for i in range(len(content_words)):
      if content_words[i] == '<VERB>':
        content_words[i] = random.choice(verb_list)
    return " ".join(content_words)
  
print(change_adjective(), change_noun(), change_verb())