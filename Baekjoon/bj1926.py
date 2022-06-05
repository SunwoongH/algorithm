'''
Created by sunwoong on 2022/06/05
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

label = result = 0
move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
def bfs(r: int, c: int) -> int:
    count = 0
    queue = collections.deque([(r, c)])
    board[r][c] = 0
    while queue:
        r, c = queue.popleft()
        count += 1
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m and board[dr][dc] == 1:
                board[dr][dc] = 0
                queue.append((dr, dc))
    return count

for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            label += 1
            result = max(result, bfs(r, c))
print(label, result, sep='\n')