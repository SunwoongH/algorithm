'''
Created by sunwoong on 2025/05/12
'''
import sys
from collections import defaultdict

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

score = defaultdict(int)
seen = set(nums)

maximum = max(nums)

for num in nums:
    for i in range(2 * num, maximum + 1, num):
        if i in seen:
            score[num] += 1
            score[i] -= 1

result = list(map(lambda x: score[x], nums))
print(*result)