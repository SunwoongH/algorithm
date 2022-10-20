'''
Created by sunwoong on 2022/10/20
'''
import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for r in range(n):
    for c in range(n):
        for k in range(10):
            dr = r - k
            if dr >= 0 and board[dr][c] == k:
                dp[r][c] += dp[dr][c]
            dc = c - k
            if dc >= 0 and board[r][dc] == k:
                dp[r][c] += dp[r][dc]
print(dp[n - 1][n - 1])