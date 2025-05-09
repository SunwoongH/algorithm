'''
Created by sunwoong on 2025/05/09
'''
import sys

n = int(sys.stdin.readline())
answer = int(1e9)
colors = []
for _ in range(n):
    color = list(map(int, sys.stdin.readline().split()))
    colors.append(color)

for k in range(3):
    dp = [[0, 0, 0] for _ in range(n)]
    
    dp[0][0] = dp[0][1] = dp[0][2] = int(1e9)
    dp[0][k] = colors[0][k]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + colors[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + colors[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + colors[i][2]
    
    dp[n - 1][k] = int(1e9)

    answer = min(answer, min(dp[n - 1]))
print(answer)