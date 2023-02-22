'''
Created by sunwoong on 2023/02/23
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coins = []
dp = [sys.maxsize for _ in range(m + 1)]
dp[0] = 0
for _ in range(n):
    coin = int(input())
    coins.append(coin)
for coin in coins:
    for i in range(coin, m + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[m]) if dp[m] != sys.maxsize else print(-1)