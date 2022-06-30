'''
Created by sunwoong on 2022/06/30
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
floor = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def bfs(r: int, c: int, is_vertical: bool) -> None:
    move, target = ([(-1, 0), (1, 0)], '|') if is_vertical else ([(0, -1), (0, 1)], '-')
    floor[r][c] = 'x'
    queue = collections.deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m and floor[dr][dc] == target:
                floor[dr][dc] = 'x'
                queue.append((dr, dc))

result = 0
for r in range(n):
    for c in range(m):
        if floor[r][c] == '|':
            result += 1
            bfs(r, c, True)
        elif floor[r][c] == '-':
            result += 1
            bfs(r, c, False)
print(result)