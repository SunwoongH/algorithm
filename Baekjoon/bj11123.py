'''
Created by sunwoong on 2022/06/09
'''
import sys
import collections
from typing import List

def bfs(r: int, c: int, h: int, w: int, group: List[int]) -> List[int]:
    move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    group[r][c] = '.'
    queue = collections.deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < h and dc >= 0 and dc < w and group[dr][dc] == '#':
                group[dr][dc] = '.'
                queue.append((dr, dc))
    return group

test = int(sys.stdin.readline())
for _ in range(test):
    h, w = map(int, sys.stdin.readline().split())
    group = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    sheep_group = 0
    for r in range(h):
        for c in range(w):
            if group[r][c] == '#':
                group = bfs(r, c, h, w, group)
                sheep_group += 1
    print(sheep_group)