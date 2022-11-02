import random 

#open, read, and write file
f = open("madlibs.txt", "r") # madlibs.txt = locaton of the file. Opens file and stores in f. "r" opens in read mode.
content = f.read() 
content_words = content.split() #seperates charcters with white spaces between them

adj_list = ['stinky' , 'ugly', 'wild', 'moldy', 'violent', 'angry', 'sick', 'filthy'] #adjective list

verb_list = ['stab', 'fear', 'cook', 'swat', 'fight', 'harass', 'explode', 'hit']

noun_list = ['toes', 'idiot', 'dog','cat','bathroom','butt','cockroach','poo']

heros_list = ['Kenzie', 'Chelsea', 'Jasmine']

def change_adjective():
    for i in range(len(content_words)): #getting length of the content words(the text file) and setting it to the range of the for loop.
      if content_words[i] == '<ADJECTIVE>':# content_words[i] means the element at index 'i' of list. 'i' is the variable created for the loop
        content_words[i] = random.choice(adj_list) #replaces the index position when the statement above is True with random element from adj_list. 
    return content_words

print(change_adjective())