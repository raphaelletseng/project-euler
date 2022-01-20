#Find the sum of all the multiples of 3 or 5 below 1000.

def solution():
    sum = 0
    for x in range(1000):
        if (x%5 == 0 or x%3 == 0): sum = sum + x
    return(sum)

#ANS: 233168