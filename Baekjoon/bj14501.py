'''
Created by sunwoong on 2022/12/30
'''
import sys
input = sys.stdin.readline

n = int(input())
tasks = []
for _ in range(n):
    day, cost = map(int, input().split())
    tasks.append((day, cost))
dp = [0 for _ in range(n)]
dp[0] = tasks[0][1] if tasks[0][0] == 1 else 0
for i in range(1, n):
    if tasks[i][0] == 1:
        dp[i] = tasks[i][1] + dp[i - 1]
    else:
        dp[i] = dp[i - 1]
    for j in range(i, i - 6 if i - 6 > -2 else -1, -1):
        if tasks[j][0] == i - j + 1:
            dp[i] = max(dp[i], dp[j - 1] + tasks[j][1] if j - 1 >= 0 else tasks[j][1])
print(max(dp))