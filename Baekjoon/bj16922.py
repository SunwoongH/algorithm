'''
Created by sunwoong on 2022/10/31
'''
import sys
from itertools import combinations_with_replacement

n = int(sys.stdin.readline())
result = []
numbers = [1, 5, 10, 50]

for temp in combinations_with_replacement(range(4), n):
    sum = 0
    for i in temp:
        sum += numbers[i]
    result.append(sum)
print(len(set(result)))