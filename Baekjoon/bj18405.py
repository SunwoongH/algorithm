'''
Created by sunwoong on 2022/10/27
'''
import sys
from collections import deque
from typing import List, Tuple

def bfs(virus: List[Tuple[int]], end_time: int) -> None:
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    queue = deque(virus)
    while queue:
        number, r, c, time = queue.popleft()
        if time == end_time:
            return
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and not board[dr][dc]:
                board[dr][dc] = number
                queue.append((number, dr, dc, time + 1))

n, k = map(int, sys.stdin.readline().split())
board = []
virus = deque()
for r in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for c in range(n):
        if line[c]:
            virus.append((line[c], r, c, 0))
    board.append(line)
s, x, y = map(int, sys.stdin.readline().split())
virus = sorted(virus, key=lambda x: x[0])
bfs(virus, s)
print(board[x - 1][y - 1])