#When run, it should count from 1 to 100. If the number is divisible by 3, print "fizz" if it's divisible by 5 print "buzz" and if it's divisible by 3 and 5, print "fizzbuzz"

num = 1 # number
while num <=100:
  print(num)
  num = num + 1

  if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
  elif num % 3 == 0:
    print("fizz")
  elif num % 5 == 0:
    print("buzz")


def fizzbuzz(n):
  number = 1
  while number < n: #while loop
    print(number)
    number = number +1
  pass


#for number in range(1,n) <---- this way also works(for loop)
  #print(number)

def fizzbuzz2(n):
  for number in range(1,n):
    output = " "
  if num % 3 == 0:
    output = output +"fizz"
  if num % 5 == 0:
    output = output + "buzz"
  if output == " ":
    output = str(number)
  print(output)
  
value=20
print("Fizzbuzz up to" , value)
fizzbuzz(20)
