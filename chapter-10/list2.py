#exercises 10.4
def average(list):
  total = 0
  for number in list:
    total = total + number 
  return total / len(list)


#10.6

import random
xs = []
for i in range(3):
    xs.append(random.randint(0,50))

def sum_of_squares(xs):
  sum_of_squares = 0
  for i in xs:
    square = i ** 2 
    sum_of_squares = square +square + square
  return sum_of_squares

print(sum_of_squares(xs))