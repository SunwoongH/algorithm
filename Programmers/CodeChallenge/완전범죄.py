'''
Created by sunwoong on 2025/02/28
'''

def solution(info, n, m):
    dp = [[float('1e9') for _ in range(m)] for _ in range(len(info) + 1)]
    dp[0][0] = 0
    
    for i in range(1, len(info) + 1):
        a, b = info[i - 1]
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + a)
            if j + b < m:
                dp[i][j + b] = min(dp[i][j + b], dp[i - 1][j])
    
    answer = float('1e9')
    for i in range(m):
        answer = min(answer, dp[len(info)][i])
    
    return answer if answer < n else -1