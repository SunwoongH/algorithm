'''
Created by sunwoong on 2025/08/20
'''
import sys

t, w = map(int, sys.stdin.readline().split())
order = [0] + [int(sys.stdin.readline()) for _ in range(t)]
dp = [[0 for _ in range(w + 1)] for _ in range(t + 1)]

for i in range(1, t + 1):
    if order[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]
    for k in range(1, w + 1):
        if k % 2 == 1 and order[i] == 2:
            dp[i][k] = max(dp[i - 1][k - 1], dp[i - 1][k]) + 1
        elif k % 2 == 0 and order[i] == 1:
            dp[i][k] = max(dp[i - 1][k - 1], dp[i - 1][k]) + 1
        else:
            dp[i][k] = max(dp[i - 1][k - 1], dp[i - 1][k])

print(max(dp[t]))