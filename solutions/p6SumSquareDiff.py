# Sum of the squares of the first 10 nat numbers = 385
# Square of the sum of the first 10 nat numbers = (1 + ... + 10)^2 = 3025

#Difference between the two : 3025-385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares(x):
    total = 0
    for i in range (1, x+1):
        total = total + (i*i)
    return total

#print(sumOfSquares(10))

def squareOfSums(x):
    total = 0
    for i in range(1, x+1):
        total = total + i
    total = total * total
    return total
#print(squareOfSums(10))

def solution6():
    diff = squareOfSums(100) - sumOfSquares(100)
    return(diff)


print(solution6())
#ANS: 25164150