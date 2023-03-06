'''
Created by sunwoong on 2023/03/06
'''

def solution(n, money):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin] % 1_000_000_007
    return dp[n]