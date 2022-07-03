'''
Created by sunwoong on 2022/07/03
'''
from math import sqrt
import sys

n = int(sys.stdin.readline())
dp = [4 for _ in range(n + 1)]
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    for j in range(1, int(sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)
print(dp[n])