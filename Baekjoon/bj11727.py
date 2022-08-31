'''
Created by sunwoong on 2022/08/31
'''
import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
dp[1] = 1
if n > 1:
    dp[2] = 3
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] * 2 + dp[i - 1]
print(dp[n] % 10007)