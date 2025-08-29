'''
Created by sunwoong on 2025/08/29
'''
import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    time, count, *prev = map(int, sys.stdin.readline().split())
    dp[i] = time
    for j in prev:
        dp[i] = max(dp[i], dp[j] + time)

print(max(dp))