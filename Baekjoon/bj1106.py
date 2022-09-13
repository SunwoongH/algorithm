'''
Created by sunwoong on 2022/09/13
'''
import sys

target, n = map(int, sys.stdin.readline().split())
city = []
possible = 0
for i in range(n):
    cost, customer = map(int, sys.stdin.readline().split())
    city.append((cost, customer))
    possible = max(possible, customer)
dp = [sys.maxsize for _ in range(target + possible)]
dp[0] = 0

for i in range(target + possible):
    for cost, customer in city:
        if i - customer >= 0:
            dp[i] = min(dp[i], dp[i - customer] + cost)
print(min(dp[target:]))