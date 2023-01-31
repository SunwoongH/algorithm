'''
Created by sunwoong on 2023/01/31
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = sorted(set(coins))
dp = [sys.maxsize for _ in range(k + 1)]
dp[0] = 0
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i - coin] + 1, dp[i])
print(dp[k]) if dp[k] != sys.maxsize else print(-1)