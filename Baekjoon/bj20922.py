'''
Created by sunwoong on 2022/08/26
'''
import sys
import collections

n, k = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
count = collections.defaultdict(int)
result = 0
left = 0
for right in range(n):
    target = sequence[right]
    count[target] += 1
    while count[target] > k:
        count[sequence[left]] -= 1
        left += 1
    result = max(result, right - left + 1)
print(result)