'''
Created by sunwoong on 2022/06/23
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
soldier = [list(sys.stdin.readline().rstrip()) for _ in range(m)]

def bfs(r: int, c: int, is_enemy: bool) -> int:
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    target = 'B' if is_enemy else 'W'
    count = 0
    soldier[r][c] = 'X'
    queue = collections.deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        count += 1
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < m and dc >= 0 and dc < n and soldier[dr][dc] == target:
                soldier[dr][dc] = 'X'
                queue.append((dr, dc))
    return count ** 2

ally = enemy = 0
for r in range(m):
    for c in range(n):
        if soldier[r][c] == 'W':
            ally += bfs(r, c, False)
        elif soldier[r][c] == 'B':
            enemy += bfs(r, c, True)
print(ally, enemy)