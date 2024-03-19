'''
Created by sunwoong on 2024/03/19
'''
move = [(0, 1), (1, 0)]

def dfs(r, c, dp, puddles, m, n):
    if r == n and c == m:
        dp[r][c] = 1
        return dp[r][c]
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr <= n and 0 <= dc <= m:
            if [dc, dr] not in puddles:
                if not dp[dr][dc]:
                    dp[r][c] += dfs(dr, dc, dp, puddles, m, n)
                else:
                    dp[r][c] += dp[dr][dc] 
    return dp[r][c] % 1_000_000_007

def solution(m, n, puddles):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    return dfs(1, 1, dp, puddles, m, n)