'''
Created by sunwoong on 2023/04/24
'''
import sys

def solution(x, y, n):
    dp = [sys.maxsize for _ in range(y + 1)]
    dp[x] = 1
    for i in range(x + 1, y + 1):
        if i % 2 == 0 and i // 2 >= x and dp[i // 2] != sys.maxsize:
            dp[i] = dp[i // 2] + 1
        if i % 3 == 0 and i // 3 >= x and dp[i // 3] != sys.maxsize:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i - n >= x and dp[i - n] != sys.maxsize:
            dp[i] = min(dp[i], dp[i - n] + 1)
    return dp[y] - 1 if dp[y] != sys.maxsize else -1