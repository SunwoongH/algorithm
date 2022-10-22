'''
Created by sunwoong on 2022/10/22
'''
import sys
from typing import List, Tuple
from collections import deque

PROMISING = 2
CHEEZE = 1
                
def find_cheeze() -> List[Tuple[int]]:
    cheeze = []
    for r in range(n):
        for c in range(m):
            if board[r][c] == CHEEZE:
                cheeze.append((r, c))
    return cheeze

def is_promising(promising: List[Tuple[int]]) -> None:
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque(promising)
    for r, c in promising:
        visited[r][c] = True
        board[r][c] = PROMISING
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and not board[dr][dc] and not visited[dr][dc]:
                board[dr][dc] = PROMISING
                visited[dr][dc] = True
                queue.append((dr, dc))
                
def melt_cheeze(cheeze: List[Tuple[int]]) -> Tuple[List[Tuple[int]]]:
    unmelted_cheeze = []
    promising = []
    queue = deque(cheeze)
    while queue:
        r, c = queue.popleft()
        is_melt = False
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and board[dr][dc] == PROMISING:
                is_melt = True
                break
        if is_melt:
            promising.append((r, c))
            board[r][c] = 0
        else:
            unmelted_cheeze.append((r, c))
    return unmelted_cheeze, promising

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
time = 0
cheeze = find_cheeze()
prev_cheeze_count = len(cheeze)
promising = [(0, 0)]
while cheeze:
    is_promising(promising)
    cheeze, promising = melt_cheeze(cheeze)
    time += 1
    if not cheeze:
        break
    prev_cheeze_count = len(cheeze)
print(time, prev_cheeze_count, sep='\n')