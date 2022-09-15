def is_even(n):
  if n % 2 ==0:
    return True #do not print true...RETURN it 
  else:
    return False


  """
  n: an interger value
  returns: true if n is even, false otherwise 
  """
def is_odd(n):
 return not(is_even(n)) 
# will give the opposite of not even. its odd if it it not even 

def isRightAngle(a,b,c): #c is the longest
  sum = a*a + b*b
  return a*a + b*b == c*c
  
def isRightAngle2(a,b,c):
  return isRightAngle(a,b,c) or \
          isRightAngle(b,c,a) or \
          isRightAngle(a,c,b)
  

  




print('even tests')
result = is_even(10)
print('result for 10 is: ', result)
result = is_even(11)
print('result for 11 is: ', result)

print('odd tests')
result = is_odd(10)
print('result for 10 is: ', result)
result = is_odd(11)
print('result for 11 is: ', result)

print(isRightAngle)