'''
Created by sunwoong on 2022/06/14
'''
import sys
import collections
from typing import Tuple

r, c = map(int, sys.stdin.readline().split())
garden = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

def bfs(y: int, x: int) -> Tuple[int, bool]:
    wolf = sheep = 0
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    queue = collections.deque([(y, x)])
    if garden[y][x] == 'v':
        wolf += 1
    elif garden[y][x] == 'o':
        sheep += 1
    garden[y][x] = '#'
    while queue:
        y, x = queue.popleft()
        for oper in move:
            dy = y + oper[0]
            dx = x + oper[1]
            if dy >= 0 and dy < r and dx >= 0 and dx < c and garden[dy][dx] != '#':
                if garden[dy][dx] == 'v':
                    wolf += 1
                elif garden[dy][dx] == 'o':
                    sheep += 1
                garden[dy][dx] = '#'
                queue.append((dy, dx))
    return (wolf, True) if wolf >= sheep else (sheep, False)

wolf = sheep = 0
for y in range(r):
    for x in range(c):
        if garden[y][x] != '#':
            count, is_wolf = bfs(y, x)
            if is_wolf:
                wolf += count
            else:
                sheep += count
print(sheep, wolf)