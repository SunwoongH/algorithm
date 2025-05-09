'''
Created by sunwoong on 2025/05/09
'''
from collections import deque

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
mmove = [(2, 0), (-2, 0), (0, -2), (0, 2)]

def bfs(distance, board, n, m):
    queue = deque([(1, 1, 1)])
    distance[1][1][0] = 0
    while queue:
        r, c, item = queue.popleft()
        if r == m and c == n:
            return min(distance[r][c])
        
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 < dr <= m and 0 < dc <= n and board[dr][dc] != 1:
                if item == 1:
                    if distance[dr][dc][0] > distance[r][c][0] + 1:
                        distance[dr][dc][0] = distance[r][c][0] + 1
                        queue.append((dr, dc, item))
                else:
                    if distance[dr][dc][1] > distance[r][c][1] + 1:
                        distance[dr][dc][1] = distance[r][c][1] + 1
                        queue.append((dr, dc, item))
        if item == 1:
            for oper in mmove:
                dr = r + oper[0]
                dc = c + oper[1]
                if 0 < dr <= m and 0 < dc <= n and board[dr][dc] != 1:
                    if distance[dr][dc][1] > distance[r][c][0] + 1:
                        distance[dr][dc][1] = distance[r][c][0] + 1
                        queue.append((dr, dc, 0))
    
    return -1 

def solution(n, m, hole):
    distance = [[[int(1e9), int(1e9)] for _ in range(n + 1)] for _ in range(m + 1)]
    board = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for c, r in hole:
        board[r][c] = 1
    return bfs(distance, board, n, m)
