'''
Created by sunwoong on 2022/08/21
'''
import sys

test = int(sys.stdin.readline())
dp = [[0 for _ in range(30)] for _ in range(30)]
for i in range(1, 30):
    dp[1][i] = i
    dp[i][i] = 1
for r in range(2, 30):
    for c in range(r + 1, 30):
        dp[r][c] = dp[r][c - 1] + dp[r - 1][c - 1]
        
for _ in range(test):
    n, m = map(int, sys.stdin.readline().split())
    print(dp[n][m])