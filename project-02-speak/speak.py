f = open("input.txt", "r")
content = f.read()  #reads text file after opening 
content_words = content.split() #seperates charcters with white spaces between them

pirate_dic = {"hey" :"'ay","friends":"mates","friend" :"mate","buddy":"matey","buddys":"mateys","is":"be","my":"me","and":"an'","were":"was","talking":"blabberin'","going":"goin'","very":"mighty","speaking":"speakin'","of":"o'","you":"ye","join":"board"}


def pirate_trans():
  for x in range(len(content_words)): #getting length of the content words(the text file) and setting it to the range of the for loop.
    for y in range(len(pirate_dic)): #nested for loop. After going through each element(x), goes through each element(y) too.
      if content_words[x] == pirate_dic[y]: # if the element at index 'x' of list and element at index 'y' of list =.
       content_words[x] == pirate_dic.get(content_words[x])
  return (" ".join(content_words).capitalize()) #capitalizes first letter and joins back with spaces
    
    