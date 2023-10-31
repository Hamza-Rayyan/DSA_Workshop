# This is merge sort alg which takes a list 'L' and two more parameters the 'left' and 'right' most positions and returns a single sorted list.
# why merge_sort? its 1000 times faster than selection and insertion sort.

def mergesort(L,left,right):
    if right-left <= 1:
        return(L[left:right])

    elif right-left > 1:
        mid = (left + right)//2

        l = mergesort(L,left,mid)
        r = mergesort(L,mid,right)
        return(merge(l,r))

def merge(L,R):
    (c,m,n) = ([],len(L),len(R))
    (i,j) = (0,0)
    while i < m and j < n:
        if  L[i] == R[j]:
            c.append(L[i])
            j = j + 1
            i= i+1
        if i == m:
            c.append(R[j])
            j = j + 1
        elif j == n:
            c.append(L[i])
            i +=1
        elif L[i] <= R[j]:
            c.append(L[i])
            i = i + 1
        elif L[i] > R[j]:
            c.append(R[j])
            j = j + 1
        
    return(c)
