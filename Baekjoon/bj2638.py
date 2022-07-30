'''
Created by sunwoong on 2022/07/30
'''
import sys
import collections
from typing import List, Tuple

def outside_check(r: int, c: int) -> None:
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = collections.deque([(r, c)])
    if board[r][c] == 0:
        board[r][c] = -1
    visited[r][c] = True
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m and not visited[dr][dc] and board[dr][dc] != 1:
                if board[dr][dc] == 0:
                    board[dr][dc] = -1
                visited[dr][dc] = True
                queue.append((dr, dc))
                
def cheeze_check(curr_cheeze: List[Tuple[int]]) -> List:
    queue = collections.deque(curr_cheeze)
    next_cheeze = []
    while queue:
        count = 0
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if board[dr][dc] == -1:
                count += 1
        if count < 2:
            next_cheeze.append((r, c))
        else:
            board[r][c] = 0
    return next_cheeze

n, m = map(int, sys.stdin.readline().split())
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
cheeze, board, time = [], [], 0

for r in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for c in range(m):
        if line[c] == 1:
            cheeze.append((r, c))
    board.append(line)

while cheeze:
    time += 1
    outside_check(0, 0)
    cheeze = cheeze_check(cheeze)
print(time)