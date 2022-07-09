'''
Created by sunwoong on 2022/07/09
'''
import sys

n, m = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(n + 1)]]
for _ in range(n):
    dp.append([0] + list(map(int, sys.stdin.readline().split())))
for r in range(1, n + 1):
    for c in range(1, n + 1):
        dp[r][c] += dp[r][c - 1]
for r in range(1, n + 1):
    for c in range(1, n + 1):
        dp[r][c] += dp[r - 1][c]
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)