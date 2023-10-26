#binary search is used for searching a item in list.
#binary search works on only a sorted list.


def binary_search(seq,v,l,r):

    if (r-1 == 0):
        return(False)
    mid = (l + r) //2
    if (v == seq[mid]):
        return(True)
    elif ( v < seq[mid]):
        return(binary_search(seq,v,l,mid))
    else:
        return(binary_search(seq,v,mid+1,r))
