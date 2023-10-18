# This program is to find that given a positive integer returns true, if that integer can be 
# paritioned into two prime numbers which on adding upon gives the integer that we have defined.


def factors(x):
    factor_list = []
    for i in range(1,x+1):
        if x % i == 0:
            factor_list.append(i)
    return(factor_list)

#factors(15)

def prime(x):
    return(factors(x) == [1,x])
    
# print(prime(17))

def primepartition(m):
    if m <= 2:
        return False  # Primes must be greater than 2
    for p in range(2, m):
        if prime(p):
            q = m - p
            if prime(q):
                return True
    return False

# Test cases
print(primepartition(13)) 
