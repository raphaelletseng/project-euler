#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

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
       
    
print(genPrime(2000000))
    
#ANS: 142913828922
# But omg find a faster way to do this Raph