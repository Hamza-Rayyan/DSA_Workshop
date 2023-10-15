# how to get factorial of a number


def factorial(m):
    
    if m == 1:
        return(1)
    else:
        return(m * factorial(m-1))
    


factorial(5)