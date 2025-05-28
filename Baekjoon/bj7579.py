'''
Created by sunwoong on 2025/5/28
'''
import sys

n, m = map(int, sys.stdin.readline().split())
byte = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

answer = sum(cost)
dp = [[0 for _ in range(sum(cost) + 1)] for _ in range(n + 1)]
for r in range(1, n + 1):
    for c in range(sum(cost) + 1):
        if cost[r - 1] > c:
            dp[r][c] = dp[r - 1][c]
            continue
        dp[r][c] = max(dp[r - 1][c - cost[r - 1]] + byte[r - 1], dp[r - 1][c])
        if dp[r][c] >= m:
            answer = min(answer, c)
print(answer)