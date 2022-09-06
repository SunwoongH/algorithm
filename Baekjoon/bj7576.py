'''
Created by sunwoong on 2022/09/06
'''
import sys
import collections
from typing import List

def spread(curr_ripe_tomato: List[int]) -> List[int]:
    next_ripe_tomato = []
    queue = collections.deque(curr_ripe_tomato)
    while queue:
        r, c = queue.popleft()
        tomato[r][c] = -2
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and tomato[dr][dc] == 0:
                tomato[dr][dc] = 1
                next_ripe_tomato.append((dr, dc))
    return next_ripe_tomato
                
def is_possible() -> bool:
    possible = True
    for r in range(n):
        for c in range(m):
            if tomato[r][c] == 0:
                possible = False
                break
    return possible

m, n = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
day = 0
ripe_tomato = []
for r in range(n):
    for c in range(m):
        if tomato[r][c] == 1:
            ripe_tomato.append((r, c))
while True:
    ripe_tomato = spread(ripe_tomato)
    if not ripe_tomato:
        break
    day += 1
print(day) if is_possible() else print(-1)