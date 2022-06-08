'''
Created by sunwoong on 2022/06/08
'''
import sys
import collections

m, n = map(int, sys.stdin.readline().split())
banner = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

def bfs(r: int, c: int) -> None:
    move = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    banner[r][c] = 0
    queue = collections.deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < m and dc >= 0 and dc < n and banner[dr][dc] == 1:
                banner[dr][dc] = 0
                queue.append((dr, dc))
                
label = 0
for r in range(m):
    for c in range(n):
        if banner[r][c] == 1:
            bfs(r, c)
            label += 1
print(label)