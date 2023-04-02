'''
Created by sunwoong on 2023/04/02
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(r, c):
    if dp[r][c]:
        return dp[r][c] + 1
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < n and 0 <= dc < n and board[dr][dc] > board[r][c]:
            dp[r][c] = max(dp[r][c], dfs(dr, dc))
    return dp[r][c] + 1

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
answer = 0
for r in range(n):
    for c in range(n):
        if not dp[r][c]:
            answer = max(answer, dfs(r, c))
print(answer)