# this iterate in a list to find a item's position when it find it
# return the position and breaks after the very first iteration

def find_position(l,v):
    for i in range(len(l)):
        if l[i] == v:
            pos = i
            break
    else:
        pos = -1
    return(pos)
