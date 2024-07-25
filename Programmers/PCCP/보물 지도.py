'''
Created by sunwoong on 2024/07/25
'''
from collections import deque

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
mmove = [(2, 0), (-2, 0), (0, -2), (0, 2)]

def bfs(board, n, m):
    queue = deque([[0, 0, 1]])
    visited = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(2)]
    visited[0][0][0] = visited[1][0][0] = 1
    while queue:
        r, c, is_valid = queue.popleft()
        if r == m - 1 and c == n - 1:
            return visited[1][r][c] - 1
        pos = 0 if is_valid else 1
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < m and 0 <= dc < n and not visited[pos][dr][dc] and board[dr][dc] != 1:
                visited[pos][dr][dc] = visited[pos][r][c] + 1
                queue.append([dr, dc, is_valid])
        if is_valid:
            for oper in mmove:
                dr = r + oper[0]
                dc = c + oper[1]
                if 0 <= dr < m and 0 <= dc < n and not visited[0][dr][dc] and board[dr][dc] != 1:
                    visited[is_valid][dr][dc] = visited[0][r][c] + 1
                    queue.append([dr, dc, 0])
    return -1
    
def solution(n, m, hole):
    board = [[0 for _ in range(n)] for _ in range(m)]
    for c, r in hole:
        board[r - 1][c - 1] = 1
    return bfs(board, n, m)