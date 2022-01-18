#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

def isDivisible(x):
    set = False
    while (set != True):
        for i in range(11, 21):
            if(x%i == 0): 
                set = True
            else: 
                set = False
                break
        x+=1 
    return x-1

print(isDivisible(232792560))

#if it's divisible by 20, it's divisible by 10, 5, 2
# 19, 18(9, 6, 3), 17, 16(8, 4), 15, 14(7), 13, 12, 11, 
# This is slow

#ANS: 232792560