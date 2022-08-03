'''
Created by sunwoong on 2022/08/03
'''
import sys
from typing import List

def multiplication(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum([i * j for i, j in zip(r, c)]) % 1000 for c in zip(*b)] for r in a]

def power(origin: List[List[int]], n: int) -> List[List[int]]:
    if n == 1:
        return [[c % 1000 for c in r] for r in origin]
    if n % 2 == 0:
        matrix = power(origin, n // 2)
        return multiplication(matrix, matrix)
    else:
        matrix = power(origin, n - 1)
        return multiplication(matrix, origin)
    
size, n = map(int, sys.stdin.readline().split())
origin = [list(map(int, sys.stdin.readline().split())) for _ in range(size)]
result = power(origin, n)
for line in result:
    print(*line)