'''
Created by sunwoong on 2023/01/05
'''
import sys
from math import sqrt
input = sys.stdin.readline

n = int(input())
dp = [sys.maxsize for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    if sqrt(i).is_integer():
        dp[i] = 1
        continue
    target = int(sqrt(i))
    while target > 0:
        dp[i] = min(dp[i], 1 + dp[i - pow(target, 2)])
        target -= 1
print(dp[n])