from solutions.p1x3Or5 import solution1
from solutions.p2EvenFib import solution2
from solutions.p3LargestPrimeFactor import solution3
from solutions.p4LargestPalindromeProduct import solution4
from solutions.p5SmallestMultiple import solution5
from solutions.p6SumSquareDiff import solution6
from solutions.p7oneHundrednFirstPrime import solution7
#from solutions.p8largestProductInSeries import solution8
from solutions.p9SpecialPythagTriplet import solution9
from solutions.p10SumOfPrimes import solution10


SOLUTIONS_DICT = {
    'one': 233168,
    'two': 4613732,
    'three': 6857,
    'four': 906609,
    'five': 232792560,
    'six': 25164150,
    'seven': 104743,

    'nine': 31875000,
    'ten': 142913828922
}


def test_all():
    assert solution1() == 233168
    assert solution2() == 4613732
    assert solution3() == 6857
    assert solution4() == 906609
    assert solution5(232792560) == 232792560
    assert solution6() == 25164150
    assert solution7(10001) == 104743
    #assert solution8() ==
    assert solution9() == 31875000
    assert solution10() == 142913828922






    #for key, val in SOLUTIONS_DICT.items():  
     #   assert key.solution() == val
