import math
def checkPrime(n):
    if(n<=1):
        return False
    for i in range (2,n):
        if(n%i==0):
            return False
    return True

def findPrimes(m,n):
    for i in range(m,n):
        if(checkPrime(i)):
            print(i)

def count(n):
    return math.log10(n)+1

def find(n):
    return type(n) 