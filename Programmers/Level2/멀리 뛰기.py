'''
Created by sunwoong on 2023/01/18
'''

def solution(n):
    if n == 1:
        return n
    dp = [0 for i in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    return dp[n]