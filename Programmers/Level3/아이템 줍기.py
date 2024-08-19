'''
Created by sunwoong on 2024/08/19
'''
from collections import deque

check = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 1), (-1, 1), (-1, -1)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(board, start_r, start_c, end_r, end_c):
    visited = [[0 for _ in range(102)] for _ in range(102)]
    visited[start_r][start_c] = 1
    
    queue = deque([(start_r, start_c)])
    
    while queue:
        r, c = queue.popleft()
        
        if r == end_r and c == end_c:
            return (visited[r][c] - 1) // 2
        
        for op in move:
            dr = r + op[0]
            dc = c + op[1]
            if visited[dr][dc] == 0 and board[dr][dc] == 2:
                visited[dr][dc] += visited[r][c] + 1
                queue.append((dr, dc))
    
    return -1

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0 for _ in range(102)] for _ in range(102)]
    
    for x1, y1, x2, y2 in rectangle:
        for r in range(y1 * 2, y2 * 2 + 1):
            for c in range(x1 * 2, x2 * 2 + 1):
                board[r][c] = 1
    
    for r in range(1, 101):
        for c in range(1, 101):
            if board[r][c] == 1:
                for op in check:
                    dr = r + op[0]
                    dc = c + op[1]
                    if board[dr][dc] == 0:
                        board[r][c] = 2
                        break
                    
    return bfs(board, characterY * 2, characterX * 2, itemY * 2, itemX * 2)