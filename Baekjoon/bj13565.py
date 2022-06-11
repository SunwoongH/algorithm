'''
Created by sunwoong on 2022/06/11
'''
import sys
import collections

m, n = map(int, sys.stdin.readline().split())
grid = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(m)]

def bfs(r: int, c: int) -> None:
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    queue = collections.deque([(r, c)])
    grid[r][c] = -1
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < m and dc >= 0 and dc < n and grid[dr][dc] == 0:
                grid[dr][dc] = -1
                queue.append((dr, dc))

for c in range(n):
    if grid[0][c] == 0:
        bfs(0, c)
is_success = False
for c in range(n):
    if grid[m - 1][c] == -1:
        is_success = True
        break
print('YES') if is_success else print('NO')