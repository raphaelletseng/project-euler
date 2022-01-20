from solutions.p1x3Or5 import solution1
from solutions.p2EvenFib import solution2
from solutions.p3LargestPrimeFactor import solution3
from solutions.p4LargestPalindromeProduct import solution4


SOLUTIONS_DICT = {
    'one': 233168,
    'two': 4613732,
    'three': 6857,
    'four': 906609
}


def test_all():
    assert solution1() == 233168
    assert solution2() == 4613732
    assert solution3() == 6857
    assert solution4() == 906609






    #for key, val in SOLUTIONS_DICT.items():  
     #   assert key.solution() == val
