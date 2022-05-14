'''
Created by sunwoong on 2022/05/14
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))