import random 
f = open("madlibs.txt", "r") 
content = f.read() 
content_words = content.split()

adj_list = ['stinky' , 'ugly', 'wild', 'moldy', 'violent', 'evil', 'sick', 'filthy']

verb_list = ['stab', 'fear', 'kick', 'melt', 'fight', 'snore', 'explode', 'laugh']

noun_list = ['toes', 'waste', 'dog','cat','bathroom','butt','cockroach','failure']

hero_list = ['Kenzie', 'Chelsea', 'Jasmine']


def change_adjective():
    for i in range(len(content_words)):
      if content_words[i] == '<ADJECTIVE>':
        content_words[i] = random.choice(adj_list)
    return " ".join(content_words)

def change_noun():
    for i in range(len(content_words)):
      if content_words[i] == '<NOUN>' or '<NOUN>.':
        content_words[i] = random.choice(noun_list)
    return " ".join(content_words)

def change_verb():
    for i in range(len(content_words)):
      if content_words[i] == '<VERB>' or '<VERB>.':
        content_words[i] = random.choice(verb_list)
    return " ".join(content_words)

def change_hero():
    for i in range(len(content_words)):
      if content_words[i] == '<HERO>' or '<HERO>.':
        content_words[i] = random.choice(hero_list)
    return " ".join(content_words)

change_verb() 
change_noun() 
change_adjective()
change_hero()

print(" ".join(content_words))