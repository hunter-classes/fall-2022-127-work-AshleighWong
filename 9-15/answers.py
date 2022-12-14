
#7.7 answer
from test import testEqual

def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False

testEqual(is_even(10), True)
testEqual(is_even(0)), True)
testEqual(is_even(5), False)
testEqual(is_even(1)), False)

#7.8 answers
from test import testEqual

def is_odd(n):
  return n % 2 > 0

testEqual(is_odd(5), True)
testEqual(is_odd(1), True)
testEqual(is_odd(10), False)
testEqual(is_odd(0), False)

#7.10 answers
from test import testEqual

def is_rightangled(a,b,c):
  return abs((a**2 + b**2) - (c**2)) < 0.001

testEqual(is_rightangled(3,4,5), True)
testEqual(is_rightangled(6,8,10), True)
testEqual(is_rightangled(1,2,3), False)
testEqual(is_rightangled(3.5, 4.5, 5.5), False)

#7.11 answes
from test import testEqual

def is_rightangled(a, b, c):
    is_rightangled = False

    if a > b and a > c:
        is_rightangled = abs((b**2 + c**2) - a**2) < 0.001
    elif b > a and b > c:
        is_rightangled = abs((a**2 + c**2) - b**2) < 0.001
    else:
        is_rightangled = abs((a**2 + b**2) - c**2) < 0.001
    return is_rightangled

testEqual(is_rightangled(3,4,5), True)
testEqual(is_rightangled(6,8,10), True)
testEqual(is_rightangled(1,2,3), False)
testEqual(is_rightangled(3.5, 4.5, 5.5), False)



#hello_name answers 
def hello_name(name):
  return "Hello " + name + "!"

#make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#first_two
def first_two(str):
  return str[:2]
