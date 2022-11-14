'''
Created by sunwoong on 2022/11/14
'''
import sys

n = int(sys.stdin.readline())
MOD = 1000000000
dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] 
print(sum(dp[n]) % MOD)