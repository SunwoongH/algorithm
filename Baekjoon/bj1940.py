'''
Created by sunwoong on 2022/06/24
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
table = dict()
for i, num in enumerate(nums):
    table[num] = i
count = 0
for i, num in enumerate(nums):
    target = m - num
    if target in table and table[target] > i:
        count += 1
print(count)