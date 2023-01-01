'''
Created by sunwoong on 2023/01/01
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
sequence = [(0, 0)]
table = defaultdict(list)
for i in range(n):
    day, cost = map(int, input().split())
    sequence.append((day, cost))
    if i + day <= n:
        table[i + day].append(i + 1)
dp = [0 for _ in range(n + 1)]
dp[1] = sequence[1][1] if sequence[1][0] == 1 else 0
for i in range(2, n + 1):
    dp[i] = dp[i - 1]
    for j in table[i]:
        if dp[i] < sequence[j][1] + dp[j - 1]:
            dp[i] = sequence[j][1] + dp[j - 1]
print(max(dp))