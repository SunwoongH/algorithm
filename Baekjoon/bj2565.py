'''
Created by sunwoong on 2022/11/08
'''
import sys

n = int(sys.stdin.readline())
cables = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cables.append((a, b))
cables.sort()
sequence = []
for _, b in cables:
    sequence.append(b)
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i - 1, -1, -1):
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))