#In the file mode.py, write the following functions:
#findLargest(l) which takes in a list of numbers and returns the value of the smallest number

def findLargest(l):
  max = l[0]
  for x in l:
    if x > max:
      max = x
  return max

#freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the freuqeency of v, that is, the number of times that v appears in l.
def CountFrequency(l,v):
  v = {}
  for i in l:
    v[i] = v.get(i, 0) + 1
  return v