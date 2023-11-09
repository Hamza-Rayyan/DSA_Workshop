#A list in Python can contain nested lists. The degree of nesting need
#not be uniform. For instance [1,2,[3,4,[5,6]]] is a valid Python list.
#Write a Python function flatten(l) that takes a nonempty list of lists
#and returns a simple list of all the elements in the nested lists,
#flattened out. You can make use of the following function that returns True
#if its input is of type list.


def listtype(l):
  return type(l) == type([])

l3=[]
def flatten(l4):
  for i in l4:
    if listtype(i):
      flatten(i)
    else:
      l3.append(i)
  return l3
