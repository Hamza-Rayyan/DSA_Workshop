def insertion_sort(seq):
    for slice in range(len(seq)):
        pos = slice
        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
            pos = pos-1
    return(seq)
