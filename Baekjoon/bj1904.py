'''
Created by sunwoong on 2022/11/06
'''
import sys

MOD = 15746
n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
dp[1] = 1
if n > 1:
    dp[2] = 2
    if n > 2:
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
print(dp[n])