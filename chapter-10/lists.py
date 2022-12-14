s = "this is a string"
elist = []
l1 = [12, 33, 15, 26]
l2 = ['one', 'two', 'three']
l3 = ['one', 2, 122, 33, 'something', 23]
l4 = ['one', ['a','b','c'], 5, [10,11,12]] #python list can store any type
slice = l1[3:5]
longer_string = s + s
longer_list = l1 + l3
#s[5] = 'I' <--- cant do this strings are immutable
#we have to do this:
new_string = s[:5] +'I' + s[:6] #cant change a string but can make a new string an reassign 
# on the other hand, we can change lists directly
l1[4]=9999999

def change_in_place(l,index,new_value):
    l[index]=new_value
print(l1)
change_in_place(l1,4,123)
print(l1)

# this is slightly better
def change_in_place_and_return(l,index,new_value):
    """
    THIS CHANGES l and returns it
    """ 
    l[index]=new_value
    return l

print(l1)
l2=change_in_place_and_return(l1,4,321)
print(l2)
print(l1)

print("--------------------------------------")
# this is an example of aliasing
# it can be powerful but you have to be careful
# and make sure you're not changing any lists
# that you don't want to change
l2 = l1
print("l1:",l1)
print("l2:",l2)
l1[4]=9999
print("l1:",l1)
print("l2:",l2)
print("---------------------------------------")
# this is how you would usually do a
# function to change part of a list
# when you want to follow the functional paradigm
def change_value(l,index,value):
    #result = []
    #for item in l:
        # we can take a variable like item
        # and put it in [] to make it a list
        # and then add it to result which is also a list
        #result = result + [item]
        # or we can call the list method
        # append with item as a parameter
        #result.append(item)
    
    #result = l.copy()    
    result = l[:]
    result[index]=value
    return result


l2  = change_value(l1,4,1111)
print("l1:",l1)
print("l2:",l2)