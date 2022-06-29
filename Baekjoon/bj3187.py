'''
Created by sunwoong on 2022/06/29
'''
import sys
import collections
from typing import Tuple

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def bfs(r: int, c: int, is_sheep: bool) -> Tuple[bool, int]:
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    sheep = wolf = 0
    if is_sheep:
        sheep += 1
    else:
        wolf += 1
    board[r][c] = '#'
    queue = collections.deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m and board[dr][dc] != '#':
                if board[dr][dc] == 'k':
                    sheep += 1
                elif board[dr][dc] == 'v':
                    wolf += 1
                board[dr][dc] = '#'
                queue.append((dr, dc))
    return (True, sheep) if sheep > wolf else (False, wolf)

sheep = wolf = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == 'k':
            check, count = bfs(r, c, True)
            if check:
                sheep += count
            else:
                wolf += count
        elif board[r][c] == 'v':
            check, count = bfs(r, c, False)
            if check:
                sheep += count
            else:
                wolf += count
print(sheep, wolf)