import checkPrime
import math
def prime_factors(n):
    factors = []
    if (checkPrime.checkPrime(n)):
        factors.append(n)
        return factors
    
    while(n%2==0):
        factors.append(2)
        n=n/2
    for i in range(3,int(n)+1,2):
        while(n%i==0):
            factors.append(i)
            n=n/i
    return factors

x=int(input('enter an integer: '))
print(prime_factors(x))

'''
2|__180__
2|___90__
3|___45__
3|____15__
5|_____5__
 |_____1__'''
 
 # line-5 checking if the given number is prime or not initially if prime then no other primes
 # line-9 getting all possible 2's factors therefore we are skipping at line 12 all value that are divisible by 2
 # Why int(n)+1 instead int(n) only? since period is 2, otherwise it'll give error for few number less than 15