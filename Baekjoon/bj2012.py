'''
Created by sunwoong on 2022/06/20
'''
import sys

n = int(sys.stdin.readline())
order = []
for _ in range(n):
    order.append(int(sys.stdin.readline()))
order.sort()
result = 0
for i in range(n):
    result += abs(i + 1 - order[i])
print(result)