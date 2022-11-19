'''
Created by sunwoong on 2022/11/19
'''
import sys

dp = [0 for _ in range(251)]
dp[0] = 1
dp[1] = 1
for i in range(2, 251):
    dp[i] = dp[i - 2] + dp[i - 2] + dp[i - 1]

while True:
    try:
        n = int(sys.stdin.readline())
        print(dp[n])
    except:
        break