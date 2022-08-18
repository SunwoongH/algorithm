'''
Created by sunwoong on 2022/08/18
'''
import sys

n = int(sys.stdin.readline())
dp = [False for _ in range(n)]
dp[0] = True
for i in range(1, n):
    if not dp[i - 1] or (i >= 4 and dp[i - 4]):
        dp[i] = True
print("SK") if dp[n - 1] else print("CY")