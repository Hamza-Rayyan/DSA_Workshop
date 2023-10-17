# Find the power of base number when a power number is def without using an exponent operator.

def power(base,power):
    result = 1
    for i in range(1,power+1):
        result *= base
        
    print(result)
    

power(5,3)