'''
Created by sunwoong on 2023/01/03
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
fixed_seat = [int(input()) for _ in range(m)]
fixed_seat = set(fixed_seat)
dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    if i in fixed_seat or i - 1 in fixed_seat:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 2] + dp[i - 1]
print(dp[n])