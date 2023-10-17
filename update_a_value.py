# updating a list on a particular index with a new value

def update(l,i,v):
    if i >= 0 and i <= len(l):
        l[i] = v
        print(l)
    else:
        print(False)
    
ns = [2,3,4]
z = 5
update(ns,2,z)