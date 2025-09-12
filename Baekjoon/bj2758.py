'''
Created by sunwoong on 2025/09/12
'''
import sys

test = int(sys.stdin.readline())

for _ in range(test):
    n, m = map(int, sys.stdin.readline().split())
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(m + 1):
        dp[1][i] = i

    for r in range(2, n + 1):
        for c in range(1, m + 1):
            dp[r][c] = dp[r][c - 1] + dp[r - 1][c // 2]
    
    print(dp[n][m])