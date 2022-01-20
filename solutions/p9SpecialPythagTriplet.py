#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
#a^2 + b^2 = c^2

# find the pythag triplet where a + b + c = 1000

def isPythagTrip(a, b, c):
    if (((a*a)+(b*b)) == (c*c)): return True


def equals1000 (a,b,c):
    if ((a + b + c) == 1000) : return True

def solution9():
    for a in range(150, 800):
        for b in range (150, 800):
            for c in range (150, 800):
                if( isPythagTrip (a,b,c)):
                    if (equals1000 (a,b,c)):
                        return(a*b*c)

#print(solution10())

#ANS: 31875000