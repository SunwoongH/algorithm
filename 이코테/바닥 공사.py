'''
Created by sunwoong on 2023/02/23
'''
import sys
input = sys.stdin.readline

MOD = 796_796
n = int(input())
dp = [0 for _ in range(n + 1)]
dp[0] = 1
for i in range(1, n + 1):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]
print(dp[n] % MOD)