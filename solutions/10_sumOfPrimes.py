#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
import math
from tkinter import N

def genPrime(max):
    primes = [2]
    sum = 2
    start = 3
    while(start < max):
        track = True
        for i in primes:
            if (start%i == 0): 
                track = False
                #start is not a prime
        if (track == True): 
            primes.append(start)
            print (start)
            sum = sum + start
        start= start + 1  
    return sum   
       
    
#print(genPrime(2000000))
    
#ANS: 142913828922
# But omg find a faster way to do this Raph

#Looping Algo to find primes
def isPrime(n):
    if (n == 1):
        return False
    else:
        if (n < 4): return True
        else:
            if (n%2 == 0):
                return False
            else:
                if (n<9): return True
                else:
                    if (n%3 == 0): return False
                    else:
                        r = math.floor(math.sqrt(n))
                        f = 5
                        while (f <= r):
                            if (n%f==0): 
                                return False
                            if(n%(f+2)==0): return False
                            f = f+6
                    return True

limit = 2000000
sum = 5
n = 5
while (n<= limit):
    if isPrime(n): sum = sum+n 
    n = n+2
    if (n<= limit and isPrime(n)): sum = sum +n 
    n = n+4

print(sum)

#wow this was SO much better

