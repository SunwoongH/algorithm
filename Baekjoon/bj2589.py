'''
Created by sunwoong on 2022/06/10
'''
import sys
import collections
from typing import List

h, w = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(h)]

def bfs(r: int, c: int, visited: List[int]) -> int:
    move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    queue = collections.deque([(r, c, 0)])
    count = 0
    visited[r][c] = True
    while queue:
        r, c, cnt = queue.popleft()
        count = max(count, cnt)
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < h and dc >= 0 and dc < w and board[dr][dc] == 'L' and not visited[dr][dc]:
                visited[dr][dc] = True
                queue.append((dr, dc, cnt + 1))
    return count

result = 0
for r in range(h):
    for c in range(w):
        if board[r][c] == 'L':
            if r > 0 and r < h - 1 and board[r - 1][c] == 'L' and board[r + 1][c] == 'L':
                continue
            if c > 0 and c < w - 1 and board[r][c - 1] == 'L' and board[r][c + 1] == 'L':
                continue
            visited = [[False for _ in range(w)] for _ in range(h)]
            result = max(result, bfs(r, c, visited))
print(result)