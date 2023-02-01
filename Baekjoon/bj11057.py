'''
Created by sunwoong on 2023/02/01
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [1 for _ in range(10)]
for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j - 1]
print(sum(dp) % 10007)