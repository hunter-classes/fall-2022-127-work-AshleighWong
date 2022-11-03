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
      elif content_words[i] == '<ADJECTIVE>.':
        content_words[i] = random.choice(adj_list) + "."
    return " ".join(content_words)

def change_noun():
    for i in range(len(content_words)):
      if content_words[i] == '<NOUN>':
        content_words[i] = random.choice(noun_list)
      elif content_words[i] == '<NOUN>.':
        content_words[i] = random.choice(noun_list) + "."
      if i.find(".") != -1: #find "." at the index and if it does not equal -1 it means there is a period. Helped by Mo Chaundrey 
        next_word = content_words[i] + 1
        content_words[i] + 1 = next_word.capitalize()       
    return " ".join(content_words)
  
def change_verb():
    for i in range(len(content_words)):
      if content_words[i] == '<VERB>':
        content_words[i] = random.choice(verb_list)
      elif content_words[i] == '<VERB>.':
        content_words[i] = random.choice(verb_list) + "."
    return " ".join(content_words)

def change_hero():
    for i in range(len(content_words)):
      if content_words[i] == '<HERO>':
        content_words[i] = random.choice(hero_list)
      elif content_words[i] == '<HERO>.':
        content_words[i] = random.choice(hero_list) + "."
    return " ".join(content_words)

change_verb() 
change_noun() 
change_adjective()
change_hero()

#capitalization
story = " ".join(content_words) #joining the story 
story = story.split('. ')
story = [s.capitalize() for s in story]
story = '''.
'''.join(story)

print(story)