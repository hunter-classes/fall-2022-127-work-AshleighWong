
"""
input: a string in the form "first last"
returns: a string in the form "Last, First Last"
"""
#bondify
def bondify(name):
  location = name.find(" ")
  result = name[0:location]
  last = name[location+1:].capitalize()
  result = last + "," + result + " " + last
  return result
  print(result)

"""
input: a string representing a word
returns: a new string with the word converted to piglatin

Rules:
if the first letter is a consonent, move it from the start to the end and add "ay"
so "hello" becomes "ellohay"

If the first letter is a vowel, just add "yay" to the end

try to also handle upper case words

"""
#check if first letter is a vowel 

def vowel_checker(letter):
  vowel = ('a','e','i','o','u','y')
  if letter in vowel:
    return True
  else:
    return False

#piglatin function 

def piglatin(word):
  if vowel_checker(word[0]) == True:
    print(word + "yay")
  else:
    #need to find length of word
    print(word[1:] + word[:1] + "ay")

piglatin(input("type in a word you want in piglatin! "))


#piglatin in class
#TODO
#make it work for capital letters
#ex Cable --> Ablecay
#make it work for punctuation 
#ex cable. --> Ablecay.

def piglatinfy(word):
  first = word[0]
  punctuation = '!'or '?'or '.'
  if first == 'AEIOUaeiou':
    first == word[0].upper()
    result = word[1:len(word-1)] + 'ay' + punctuation
  else:
    first==word[1].upper
    result = word[1:len(word-1)] + word[:1] + 'ay' + punctuation 
  #if
  #transform for the first letter consonant
  #else
  #or
  #transform for first letter vowel
  return result

#testing piglatinfy
test_word = "hello"
result = piglatinfy(test_word)
print(test_word, " -->", result)

test_word = "Cable"
result = piglatinfy(test_word)
print(test_word, " -->", result)

test_word = "cable."
result = piglatinfy(test_word)
print(test_word, " -->", result)

test_word = "hello!"
result = piglatinfy(test_word)
print(test_word, " -->", result)

test_word = "hello."
result = piglatinfy(test_word)
print(test_word, " -->", result)

