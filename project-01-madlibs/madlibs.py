import random 

#open, read, and write file
f = open("madlibs.txt", "r") # madlibs.txt = locaton of the file. Opens file and stores in f. "r" opens in read mode. "w" opens in write mode. "a" appends new content at end of file.
content = f.read()
content_words = content.split() #seperates charcters with white spaces between them

adj_list = ['stinky' , 'ugly', 'wild', 'moldy', 'violent', 'angry', 'sick', 'filthy']

verb_list = ['stab', 'fear', 'cook', 'swat', 'fight', 'harass', 'explode', 'hit']

noun_list = ['toes', 'idiot', 'dog','cat','bathroom','butt','cockroach','poo']

heros_list = ['Kenzie', 'Chelsea', 'Jasmine']

def change_adjective(adjective):
    for word in content_words:
      if content_words == '<ADJECTIVE>':
        result = content_words.replace(random.choice(adj_list))
    return result

    print(result)

