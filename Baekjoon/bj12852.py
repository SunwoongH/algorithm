'''
Created by sunwoong on 2022/12/31
'''
import sys
input = sys.stdin.readline

n = int(input())
path = dict()
dp = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    if i % 3 == 0:
        dp[i] = dp[i // 3] + 1
        path[i] = i // 3
    if i % 2 == 0:
        if not dp[i] or dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            path[i] = i // 2
    if not dp[i] or dp[i] > dp[i - 1] + 1:
        dp[i] = dp[i - 1] + 1
        path[i] = i - 1
route = []
i = n
while i != 1:
    route.append(i)
    i = path[i]
route.append(i)
print(dp[n])
print(*route)