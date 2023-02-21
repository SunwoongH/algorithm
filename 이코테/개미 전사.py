'''
Created by sunwoong on 2023/02/21
'''
import sys
input = sys.stdin.readline

n = int(input())
foods = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = foods[0]
dp[1] = max(dp[0], foods[1])
for i in range(2, n):
    dp[i] = max(foods[i] + dp[i - 2], dp[i - 1])
print(dp[n - 1])