'''
Created by sunwoong on 2022/09/10
'''
import sys
import collections
from typing import List, Tuple

def flood(is_island: List[int]) -> List[int]:
    queue = collections.deque(is_island)
    flood_island = []
    while queue:
        r, c = queue.popleft()
        count = 0
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr < 0 or dr >= n or dc < 0 or dc >= m or island[dr][dc] == '.':
                count += 1
        if count > 2:
            island[r][c] = 'O'
            flood_island.append((r, c))
    return flood_island
            
def cutting() -> Tuple[int]:
    r_left = r_right = None
    for i, line in enumerate(island):
        if ''.join(line) != '.' * len(line):
            if r_left is None:
                r_left = i
            else:
                r_right = i
    c_left = c_right = None
    for i, line in enumerate(zip(*island)):
        if ''.join(line) != '.' * len(line):
            if c_left is None:
                c_left = i
            else:
                c_right = i
    r_left, r_right = (r_left, r_right) if r_right else (r_left, r_left)
    c_left, c_right = (c_left, c_right) if c_right else (c_left, c_left)
    return r_left, r_right, c_left, c_right
            
n, m = map(int, sys.stdin.readline().split())
island = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
is_island = []
for r in range(n):
    for c in range(m):
        if island[r][c] == 'X':
            is_island.append((r, c))
flood_island = flood(is_island)
for r, c in flood_island:
    island[r][c] = '.'
r_left, r_right, c_left, c_right = cutting()
for r in range(r_left, r_right + 1):
    print(''.join(island[r][c_left:c_right + 1]))