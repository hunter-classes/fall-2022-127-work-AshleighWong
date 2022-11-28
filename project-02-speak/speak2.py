#pirate translator -- solo project
#Extras:
  #multiple translators (pirate, brooklyn, swedish chef)
  #capitalization 
pirate_dic = {"hey" :"'ay",
              "friends":"mates",
              "friend" :"mate",
              "buddy":"matey",
              "buddys":"mateys",
              "is":"be",
              "My":"Me",
              "and":"an'",
              "were":"was",
              "talking":"blabberin'",
              "going":"goin'",
              "very":"mighty",
              "speaking":"speakin'",
              "of":"o'",
              "you":"ye",
              "join":"board"}


brook_dic = {"isn't":"ain't",
             "other":"othuh",
             "talking":"tawhkin'",
             "going":"gonna",
             "thin":"tink",
             "speaking":"speakin'",
             "later":"latuh",
             "you":"yuh"}
             

Schef_dic = {"fine":"feene-a",
             'day':'dey',
             'other':'ouzeer',
             'buddy': 'buoddy',
             'and':'und',
             'were':'vere-a',
             'talking':'telkeeng',
             'about':'ibuout',
             'going':'guing',
             'to':'tu',
             'take':'teke-a',
             'swim':'svim',
             'think':'zeenk',
             'will':'vill',
             'be':'be-a',
             'very':'fery',
             'fun':'fuon',
             'speaking':'speekeng',
             'off':'ouff',
             'come':'cume-a',
             'join':'juin',
             'if':'iff',
             'you':'yuou',
             'would':'vuould',
             'like':'leeke-a',
             'catch':'cetch',
             'later':'leter'}
            


#open text file as a read 
f = open("input.txt", "r")
content = f.read()  #reads text file after opening 
content_words = content.split() #seperates charcters with white spaces between them

#pirate trasnlatior
def pirate_trans():
  for i in range(len(content_words)): #goes through each element in the list content_words
    word = content_words[i]
    if word in pirate_dic: #finding if the  value indexed at 'i' is in the pirate dictionary
      content_words[i] = pirate_dic[content_words[i]] # replaces the word from 
  return ' '.join(content_words)

#brooklyn translator 
def brook_trans():
  for i in range(len(content_words)):
    word = content_words[i]
    if word in brook_dic:
      content_words[i] = brook_dic[content_words[i]]
  return ' '.join(content_words)


#swedish chef translator 
def Schef_trans():
  for i in range(len(content_words)):
    word = content_words[i]
    if word in Schef_dic:
      content_words[i] = Schef_dic[content_words[i]]
      if word in Schef_dic.capitalize:
        content_words[i] = Schef_dic[content_words[i]].capitalize
  return ' '.join(content_words)
  

def option():
  choice = input('What translator would you like to pick? A: pirate, brooklyn, or chef ')
  if choice =='pirate':
    print(pirate_trans())
  elif choice =='brooklyn':
    print(brook_trans())
  else:
    print(Schef_trans() + " Bork! Bork! Bork!")

option()