#mapping functions

def apply(f,x,n):
    res = x
    for i in range(n):
        res = f(res)
    return(res)
def square(x):
    return(x*x)
