'''
Created by sunwoong on 2022/08/12
'''
import sys
from itertools import combinations

n = int(sys.stdin.readline())
result = sys.maxsize
food = []
for _ in range(n):
    food.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n + 1):
    for items in combinations(food, i):
        sour = 1
        bitter = 0
        for item in items:
            sour *= item[0]
            bitter += item[1]
        result = min(result, abs(sour - bitter))
print(result)