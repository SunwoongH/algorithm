'''
Created by sunwoong on 2022/06/19
'''
import sys

n = int(sys.stdin.readline())
rope = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)

result = weight = 0
for i in range(n):
    weight = rope[i] * (i + 1)
    result = max(result, weight)
print(result)