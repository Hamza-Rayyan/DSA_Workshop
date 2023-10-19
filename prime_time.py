#This particular block will return factors
def factors(n):
    f_list = []
    for i in range(1,n+1):
        if n % i == 0:
            f_list.append(i)
    return(f_list)


#This block will return the true if the number entered is true
def primes(n):
    return(factors(n) == [1,n])


# the block will return list of all the prime numbers till the number entered.
def prime_upto_n(n):
    prime_list = []
    for i in range(1,n+1):
        if primes(i):
            prime_list.append(i)
    return(prime_list)

# the will return the list of n primes numbera like if you want the first 20
# primes numbers this will return a list of first 20 primes no.

def nprimes(n):
    (count, i, plist) = (0,1,[])
    while (count < n):
        if primes(i):
            (count,plist) = (count + 1,plist+[i])
        i = i + 1
    return(plist)

    
