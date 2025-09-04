'''
Created by sunwoong on 2025/09/04
'''
import sys

n, m = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))
costs = [0 for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]

for _ in range(m):
    i, w = map(int, sys.stdin.readline().split())
    costs[i] += w

for i in range(2, n + 1):
    dp[i] = costs[i]
    dp[i] += dp[nums[i]]

print(*dp[1:])