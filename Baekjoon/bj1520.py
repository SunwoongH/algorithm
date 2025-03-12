'''
Created by sunwoong on 2025/03/12
'''
import sys
sys.setrecursionlimit(10 ** 6)

m, n = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
counting = [[-1 for _ in range(n)] for _ in range(m)]

def dfs(board, r, c):
    if r == m - 1 and c == n - 1:
        counting[r][c] = 1
        return counting[r][c]
    counting[r][c] = 0
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < m and 0 <= dc < n:
            if board[dr][dc] < board[r][c]:
                if counting[dr][dc] == -1:
                    counting[r][c] += dfs(board, dr, dc)
                else:
                    if counting[dr][dc] > 0:
                        counting[r][c] += counting[dr][dc]
    return counting[r][c]

print(dfs(board, 0, 0))