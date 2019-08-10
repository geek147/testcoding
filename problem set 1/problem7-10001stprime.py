def primecount(n) :
    count = 0
    numberPrime = 1
    while (count  < n):
        numberPrime +=1
        if isPrime(numberPrime):
            count+=1
    return numberPrime

def isPrime(n) :  
    if (n <= 1) :  
        return False
    if (n <= 3) :  
        return True
    
    #check if we can skip 5 first number 
    if (n % 2 == 0 or n % 3 == 0) :  
        return False
    
    i = 5
    while(i * i <= n) :  
        if (n % i == 0 or n % (i + 2) == 0) :  
            return False
        i = i + 6
    
    return True

#change the value here    
print(primecount(10001))

