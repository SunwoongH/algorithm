'''
Created by sunwoong on 2022/06/28
'''
import sys
import collections
from typing import List

n, m = map(int, sys.stdin.readline().split())
board, shark = [], []
for r in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for c in range(m):
        if line[c] == 1:
            shark.append((r, c))
    board.append(line)

def bfs(shark: List[int]) -> int:
    move = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = collections.deque()
    for baby in shark:
        visited[baby[0]][baby[1]] = 1
        queue.append(baby)
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m and not visited[dr][dc]:
                visited[dr][dc] = visited[r][c] + 1
                queue.append((dr, dc))
    return max(map(max, visited)) - 1
print(bfs(shark))