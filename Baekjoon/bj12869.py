'''
Created by sunwoong on 2025/03/06
'''
import sys
from itertools import permutations

n = int(sys.stdin.readline())
scv = list(map(int, sys.stdin.readline().split()))
scv.extend([0, 0])

dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
dp[scv[0]][scv[1]][scv[2]] = 1

for i in range(60, -1, -1):
    for j in range(60, -1, -1):
        for k in range(60, -1, -1):
            if dp[i][j][k] > 0:
                for case in permutations([9, 3, 1], 3):
                    di = i - case[0] if i - case[0] >= 0 else 0
                    dj = j - case[1] if j - case[1] >= 0 else 0
                    dk = k - case[2] if k - case[2] >= 0 else 0
                    if dp[di][dj][dk] == 0 or dp[di][dj][dk] > dp[i][j][k] + 1:
                        dp[di][dj][dk] = dp[i][j][k] + 1

print(dp[0][0][0] - 1)