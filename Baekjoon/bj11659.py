'''
Created by sunwoong on 2022/07/27
'''
import sys

n, m = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))
for i in range(1, n + 1):
    nums[i] += nums[i - 1]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(nums[j] - nums[i - 1])