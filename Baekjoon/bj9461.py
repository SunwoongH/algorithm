'''
Created by sunwoong on 2022/10/26
'''
import sys

test = int(sys.stdin.readline())
for _ in range(test):
    n = int(sys.stdin.readline())
    if n < 4:
        print(1)
    else:
        dp = [0 for _ in range(n + 1)]
        dp[1] = dp[2] = dp[3] = 1
        for i in range(4, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2]
        print(dp[n])