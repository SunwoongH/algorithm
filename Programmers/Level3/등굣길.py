'''
Created by sunwoong on 2022/12/01
'''

def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    water = set()
    move = [(-1, 0), (0, -1)]
    for puddle in puddles:
        water.add(tuple(puddle))
    for r in range(n):
        for c in range(m):
            if (c + 1, r + 1) in water:
                continue
            for oper in move:
                dr = r + oper[0]
                dc = c + oper[1]
                if 0 <= dr < n and 0 <= dc < m:
                    dp[r][c] += dp[dr][dc]
            dp[r][c] %= 1000000007
    return dp[n - 1][m - 1]