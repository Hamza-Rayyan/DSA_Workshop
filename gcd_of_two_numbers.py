# This helps you to find the greatest common factor between two numbers.

def gcd(m,n):
    
    for i in range(1,min(m,n)+1):
        if m % i == 0 and n % i == 0: 
            mrcf = i
    print(mrcf)


gcd(14,63)
