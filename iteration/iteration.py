#this is a for each loop -->
for counter in range(2,20,3): #go from 2-20 by 3's
  print (counter)
  
print("............")
for counter in range(5): #
  print(counter)

print("............")
for counter in [0,1,2,3,4]: #sets counter to each item in the list 
  print(counter)

print("............")
for letter in "this is a sentence":
  print(letter)

#while loop
#while True:
  print("this loop")
  print("will never end")

while False:
  print("this loop")
  print("will not loop")

loop_counter = 0
while random.randrange(0,100) < 80:
  print("hello" , loop_counter)
  loop_counter = loop_counter + 1
print('the above loop ran many times', loop_counter)
print('.............')



#while loop as a counting loop
#first set up a variable to hold the count
i = 0
#the use the boolean to indicate when to stop 
while i < 5:
  print(i)
i = i + 1 #dont forget to change the variable so you eventually stop 

#or count down
print('..............')
i = 5
while i > 0:
  print(i)
i = i - 1 

#you can also traverse over a string 
s = 'hello world'
i =0
while i < len(s):
  print(s[i])
  i = i + 1

print('............')
for i in range(   len(s)  ):
  print(s[i])