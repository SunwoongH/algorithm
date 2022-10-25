'''
Created by sunwoong on 2022/10/25
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if sequence[j] > sequence[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))