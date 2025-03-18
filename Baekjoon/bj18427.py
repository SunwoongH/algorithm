
'''
Created by sunwoong on 2025/03/18
'''
import sys

n, m, h = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(1001)] for _ in range(51)]
dp[0][0] = 1
for i in range(n):
    blocks = list(map(int, sys.stdin.readline().split()))
    for j in range(1001):
        dp[i + 1][j] = dp[i][j]
    for block in blocks:
        for j in range(block, 1001):
            dp[i + 1][j] += dp[i][j - block]
print(dp[n][h] % 10007)