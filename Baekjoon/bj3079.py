'''
Created by sunwoong on 2022/12/19
'''
import sys
from math import ceil
input = sys.stdin.readline

n, m = map(int, input().split())
desks = []
for _ in range(n):
    time = int(input())
    desks.append(time)
low, high = 1, ceil(m * max(desks) / n)
while low <= high:
    mid = (low + high) // 2
    count = 0
    for time in desks:
        count += mid // time
    if count >= m:
        high = mid - 1
    else:
        low = mid + 1
print(low)