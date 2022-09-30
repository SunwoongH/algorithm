'''
Created by sunwoong on 2022/10/01
'''
import sys
import collections
from typing import List, Tuple

RIPE = 1
UNRIPE = 0

def find_ripe_tomatoes() -> List[Tuple[int]]:
    ripe_tomatoes = []
    for k in range(h):
        for r in range(n):
            for c in range(m):
                if storage[k][r][c] == RIPE:
                    ripe_tomatoes.append((k, r, c, 0))
    return ripe_tomatoes
                
def bfs(ripe_tomatoes: List[Tuple[int]]) -> int:
    queue = collections.deque(ripe_tomatoes)
    day = 0
    while queue:
        k, r, c, day = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            dk = k + oper[2]
            if 0 <= dr < n and 0 <= dc < m and 0 <= dk < h and storage[dk][dr][dc] == UNRIPE:
                storage[dk][dr][dc] = RIPE
                queue.append((dk, dr, dc, day + 1))
    return day

def calculate_date(ripe_tomatoes: List[Tuple[int]]) -> None:
    day = bfs(ripe_tomatoes)
    is_possible = True
    for k in range(h):
        for r in range(n):
            for c in range(m):
                if storage[k][r][c] == UNRIPE:
                    is_possible = False
                    break
    print(day) if is_possible else print(-1)
    
storage = []
move = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]
m, n, h = map(int, sys.stdin.readline().split())
for _ in range(h):
    tomato = []
    for _ in range(n):
        tomato.append(list(map(int, sys.stdin.readline().split())))
    storage.append(tomato)
calculate_date(find_ripe_tomatoes())