'''
Created by sunwoong on 2024/03/19
'''

def solution(triangle):
    length = len(triangle[-1])
    dp = [[0 for _ in range(length + 2)] for _ in range(length + 1)]
    for r in range(1, length + 1):
        for c in range(1, r + 1):
            dp[r][c] = max(dp[r - 1][c], dp[r - 1][c - 1]) + triangle[r - 1][c - 1]
    return max(dp[-1])