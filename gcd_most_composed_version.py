# the previous version was a navie one it will iterate the loop a
# billion time if the numbers are in billion where as,
# Using Euclids algorithm it takes only ten steps which is a huge diffrence.

def gcd(m,n):
    if m < n:
        (m,n) = (n,m)
    if (m%n) == 0:
        return(n)
    else :
        return(gcd(n,m%n))
