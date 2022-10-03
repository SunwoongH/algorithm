'''
Created by sunwoong on 2022/10/03
'''
import sys
import collections
from copy import deepcopy

def case_1(r: int, c: int, color: str):
    queue = collections.deque([(r, c)])
    color_1[r][c] = EMPTY
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and color_1[dr][dc] in color:
                color_1[dr][dc] = EMPTY
                queue.append((dr, dc))

def case_2(r: int, c: int, color: str):
    color = 'B' if color == 'B' else 'RG'
    queue = collections.deque([(r, c)])
    color_2[r][c] = EMPTY
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and color_2[dr][dc] in color:
                color_2[dr][dc] = EMPTY
                queue.append((dr, dc))

EMPTY = 'X'
n = int(sys.stdin.readline())
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
color_1 = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
color_2 = deepcopy(color_1)
case_1_count = case_2_count = 0
for r in range(n):
    for c in range(n):
        if color_1[r][c] != EMPTY:
            case_1(r, c, color_1[r][c])
            case_1_count += 1
        if color_2[r][c] != EMPTY:
            case_2(r, c, color_2[r][c])
            case_2_count += 1
print(case_1_count, case_2_count)