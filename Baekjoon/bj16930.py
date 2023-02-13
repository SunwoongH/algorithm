'''
Created by sunwoong on 2023/02/13
'''
import sys
from collections import deque
input = sys.stdin.readline

PROMISING = '.'
WALL = '#'
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(start_r, start_c, end_r, end_c, k):
    queue = deque([(start_r, start_c)])
    while queue:
        r, c = queue.popleft()
        if r == end_r and c == end_c:
            return visited[r][c]
        for oper in move:
            for i in range(1, k + 1):
                dr = r + oper[0] * i
                dc = c + oper[1] * i
                if dr < 0 or dr >= n or dc < 0 or dc >= m or board[dr][dc] == WALL or (visited[dr][dc] and visited[r][c] == visited[dr][dc]):
                    break
                if not visited[dr][dc]:
                    visited[dr][dc] = visited[r][c] + 1
                    queue.append((dr, dc))
    return -1

n, m, k = map(int, input().split())
board = []
for _ in range(n):
    line = list(input().rstrip())
    board.append(line)
start_r, start_c, end_r, end_c = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
print(bfs(start_r - 1, start_c - 1, end_r - 1, end_c - 1, k))