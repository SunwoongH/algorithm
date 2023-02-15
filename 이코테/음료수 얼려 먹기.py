'''
Created by sunwoong on 2023/02/15
'''
import sys
from collections import deque
input = sys.stdin.readline

PROMISING = '0'
VISITED = '2'
WALL = '1'

def bfs(start_r, start_c):
    queue = deque([(start_r, start_c)])
    board[start_r][start_c] = VISITED
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and board[dr][dc] == PROMISING:
                board[dr][dc] = VISITED
                queue.append((dr, dc))

n, m = map(int, input().split())
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
board = [list(input().rstrip()) for _ in range(n)]
count = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == PROMISING:
            bfs(r, c)
            count += 1
print(count)