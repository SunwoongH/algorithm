'''
Created by sunwoong on 2023/03/17
'''
import sys
input = sys.stdin.readline

def dfs(r, c):
    visited[r][c] = True
    if r == m - 1 and c == n - 1:
        count[r][c] = 1
        return count[r][c]
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < m and 0 <= dc < n and board[dr][dc] < board[r][c]:
            if not visited[dr][dc]:
                count[r][c] += dfs(dr, dc)
            else:
                count[r][c] += count[dr][dc]
    return count[r][c]

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
count = [[0 for _ in range(n)] for _ in range(m)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
print(dfs(0, 0))