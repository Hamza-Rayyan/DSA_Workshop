#This is an Quick Sort algorithm represent in python that takes O(n log n).


def quicksort(A,l,r):  # sort A[l:r]
    if r-l <= 1:
        return()
    G = l+1  #pivot point A[l]
    for R in range(l+1,r):
        if A[R] < A[l]:
            (A[G],A[R]) = (A[R],A[G])
            G = G + 1
    (A[l],A[G-1]) = (A[G-1],A[l]) # Move pivot into place
    quicksort(A,l,G)    #Recursion calls
    quicksort(A,G,r)
    return(A)
    
