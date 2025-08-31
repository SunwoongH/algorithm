'''
Created by sunwoong on 2025/08/31
'''
import sys

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]

dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))