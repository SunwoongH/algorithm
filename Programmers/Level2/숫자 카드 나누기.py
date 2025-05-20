'''
Created by sunwoong on 2025/05/20
'''
from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    gcd_a = reduce(gcd, arrayA)
    gcd_b = reduce(gcd, arrayB)
    
    gcd_a_promising = all(num % gcd_a != 0 for num in arrayB)
    gcd_b_promising = all(num % gcd_b != 0 for num in arrayA)
    
    if gcd_a_promising and gcd_b_promising:
        return max(gcd_a, gcd_b)
    elif not gcd_a_promising and gcd_b_promising:
        return gcd_b
    elif gcd_a_promising and not gcd_b_promising:
        return gcd_a
    return 0