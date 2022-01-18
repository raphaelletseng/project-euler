#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?




def isPrime(p):
    return all(p%i for i in range (2, p-1))

def prime(p):
    return next(p//i for i in range (1, p) if p% i == 0 and isPrime(p//i))

#print(prime(600851475143))

def findPrimes(p):
    primes = []
    for i in range(2, p+1):
        if (p%i == 0):
            count = 1
            for j in range(2, (i//2 + 1)):
                if(i%j == 0):
                    count = 0
                    break
            if (count == 1):
                print(i)
                primes.append(i)
    return primes[len(primes)-1]



print(findPrimes(600851475143))

#ANS: 6857
