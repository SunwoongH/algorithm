'''
Created by sunwoong on 2025/05/13
'''

import sys

string = sys.stdin.readline().rstrip()

promising = [[False for _ in range(len(string))] for _ in range(len(string))]
dp = [int(1e9) for _ in range(len(string) + 1)]

for i in range(len(string)):
    promising[i][i] = True

for i in range(1, len(string)):
    if string[i - 1] == string[i]:
        promising[i - 1][i] = True

for i in range(3, len(string) + 1):
    for j in range(len(string) - i + 1):
        if string[j] == string[j + i - 1] and promising[j + 1][j + i - 2]:
            promising[j][j + i - 1] = True

dp[-1] = 0
for i in range(len(string)):
    for j in range(i + 1):
        if promising[j][i]:
            dp[i] = min(dp[i], dp[j - 1] + 1)

print(dp[len(string) - 1])