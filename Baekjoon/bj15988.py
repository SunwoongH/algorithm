'''
Created by sunwoong on 2023/01/02
'''
import sys
input = sys.stdin.readline

test = int(input())
data = [int(input()) for _ in range(test)]
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1_000_000_009
for num in data:
    print(dp[num])