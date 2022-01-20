#A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

max = 500005

def isPal(p):
    num = [int(x) for x in str(p)]
    point = 0
    while(point < (len(str(p))/2)):
        if (num[point] != num[len(num)-1-point]): return False
        else: point+=1
    return True

for n1 in range(100, 1000):
    for n2 in range (100, 1000):
        sum = n1*n2
        if(isPal(sum) and sum > max):
            max = sum
        
print(max)

#ANS: 906609

