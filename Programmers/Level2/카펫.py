'''
Created by sunwoong on 2023/01/18
'''
from math import sqrt

def solution(brown, yellow):
    start = sqrt(yellow)
    start = int(start) if start.is_integer() else int(start) + 1
    for i in range(start, yellow + 1):
        if yellow % i == 0:
            if (i + yellow // i) * 2 + 4 == brown:
                return [i + 2, yellow // i + 2]