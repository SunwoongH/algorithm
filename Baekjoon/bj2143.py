'''
Created by sunwoong on 2025/03/18
'''
import sys
from collections import defaultdict

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

nums = defaultdict(int)

for i in range(1, m):
    b[i] += b[i - 1]

for i in range(1, n):
    a[i] += a[i - 1]

for i in range(m):
    nums[b[i]] += 1
    for j in range(i):
        nums[b[i] - b[j]] += 1

answer = 0
for i in range(n):
    target = t - a[i]
    if target in nums:
        answer += nums[target]
    for j in range(i):
        target = t - (a[i] - a[j])
        if target in nums:
            answer += nums[target]

print(answer)