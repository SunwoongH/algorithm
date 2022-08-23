'''
Created by sunwoong on 2022/08/23
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n)]
for i in range(n):
    prev = None
    dp[i] = sequence[i]
    for j in range(i - 1, -1, -1):
        if not prev:
            if sequence[j] < sequence[i]:
                prev = j
                dp[i] = max(dp[i], dp[j] + sequence[i])
        else:
            if sequence[prev] < sequence[j] and sequence[j] < sequence[i]:
                dp[i] = max(dp[i], dp[j] + sequence[i])
                prev = j
print(max(dp))