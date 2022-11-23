'''
Created by sunwoong on 2022/11/23
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(n)]
dp[0] = 1
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if sequence[j] > sequence[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))