#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

def solution7(index):
    primes = [2]
    start = 3
    while(len(primes) < index):
        track = True
        for i in primes:
            if (start%i == 0): 
                track = False
                #start is not a prime
        if (track == True): primes.append(start)
        start= start + 1     
    #return primes       
    return primes[len(primes)-1]

#print(genPrime(10001))
    
#ANS: 104743

