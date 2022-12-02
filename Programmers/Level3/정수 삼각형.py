'''
Created by sunwoong on 2022/12/02
'''

def solution(triangle):
    dp = [[0 for _ in range(len(triangle[-1]))] for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for r in range(1, len(triangle)):
        for c in range(len(triangle[r])):
            if c == 0:
                dp[r][c] = dp[r - 1][c] + triangle[r][c]
            elif c == len(triangle[r]) - 1:
                dp[r][c] = dp[r - 1][c - 1] + triangle[r][c]
            else:
                dp[r][c] = max(dp[r - 1][c - 1], dp[r - 1][c]) + triangle[r][c]
    return max(dp[len(triangle) - 1])