'''
Created by sunwoong on 2025/03/05
'''

import sys

n = int(sys.stdin.readline())
maps = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    maps.append(line)

dp = [[[-1 for _ in range(3)] for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        if maps[r][c] == 0:
            dp[r][c][0] = 1

move = [(-1, 0), (0, -1)]

for r in range(n):
    for c in range(n):
        for k in range(3):
            prev = (k - 1 + 3) % 3
            for oper in move:
                pr = r + oper[0]
                pc = c + oper[1]
                if 0 <= pr < n and 0 <= pc < n:
                    if maps[r][c] == k and dp[pr][pc][prev] != -1:
                        dp[r][c][k] = max(dp[r][c][k], dp[pr][pc][prev] + 1)
                    else:
                        dp[r][c][k] = max(dp[r][c][k], dp[pr][pc][k])

print(max(dp[n - 1][n - 1]) if max(dp[n - 1][n - 1]) != -1 else 0)