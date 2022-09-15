s1 = "Hello World"
s2 = 'another \nstring' #n is a way of representing its character which is the new line 

s3 = """
This is a multiline string
we use triple quotes for that
"""
#'Joh)n\'s book'

s4 = s1+s2# string catenation
print(s4)
print(s1*3) # prints string 3 times

print(len(s1))
print(len("abcde"))

print(s1.upper())

print(s1.find("H")) #gives us the location of H
print(s1[3])# Gives the String of the 3rd location
print(s1[5:10]) # prints the strings from 5-10 inclusive

space_location = print(s1.find(" "))
print(space_location)
s5 = s1[space_location+1:] # nothing after the : means go to the end
print(s5)

print(s1[-1]) # another way of getting the last element